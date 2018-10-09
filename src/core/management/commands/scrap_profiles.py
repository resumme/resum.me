from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from core.models import ProviderProfile, Course, Provider, Status, CourseStatus
import requests
import timeit

class Command(BaseCommand):
    help = 'Scraps courses from codeschool'

    def handle(self, *args, **options):

        def manage_relation_course_profile(profile, course, status):
            """
            Manages the status of the relation between course and
            provider profile.

            :param profile: provider profile object
            :param course: course object
            :param status: status that is saved the relation
            :return:
            """
            CourseStatus.objects.update_or_create(profile=profile,
                                                  course=course,
                                                  status=status)

        def add_courses_to_user(user, courses, status, provider):
            """
            From a serializede course list, saves the data in
            Django models.

            :param user: user object
            :param courses: course list
            :param status: courses are saved with this status
            :param provider: course provider object
            """
            status = Status.objects.get(name=status)
            provider = Provider.objects.get(name=provider)
            profile, created = ProviderProfile.objects.get_or_create(user=user,
                                                                     provider=provider)
            for course in courses:
                new_course, created = Course.objects.get_or_create(
                    title=course.get('title'),
                    url=course.get('url'),
                    badge=course.get('badge'),
                    provider=provider
                )
                manage_relation_course_profile(profile, new_course, status)

        CODESCHOOL_URL = 'https://www.codeschool.com/users/{}.json'
        for profile in ProviderProfile.objects.all():
            try:
                if not profile.username_provider:
                    raise Exception('Username does not have a provider profile')
                url = CODESCHOOL_URL.format(profile.username_provider)
                response = requests.get(url).json()
                courses = response.get('courses')
                add_courses_to_user(user=profile.user,
                                    courses=courses.get('in_progress'),
                                    status='i',
                                    provider='codeschool')

                add_courses_to_user(user=profile.user,
                                    courses=courses.get('completed'),
                                    status='c',
                                    provider='codeschool')
            except Exception as e:
                raise CommandError('Error in request {}'.format(e))
