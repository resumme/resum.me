from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient

from core.models import ProviderProfile, CourseStatus, Bio


class Command(BaseCommand):
    help = 'Saves in a local mongoDB the user profiles serialized'

    def handle(self, *args, **options):

        def serialize_user_provider_profiles(user_provider_list):
            """
            Serializes the courses of a provider profile
            :param user_provider_list: provider profile object
            :return: dictionary that contains the finished and in
            progress courses.
            """
            course_list = {}
            for user_provider_profile in user_provider_list:
                courses = CourseStatus.objects.filter(profile=user_provider_profile)

                course_list['completed'] = serialize_course_list(
                    course_list=courses.filter(status__name="c").all()
                )
                course_list['in_progress'] = serialize_course_list(
                    course_list=courses.filter(status__name="i").all()
                )
            return course_list

        def serialize_course_list(course_list):
            """
            Serializes the courses of a provider profile
            :param course_list: courses of a provider profile
            :return: list with the serialized courses
            """
            serialized_courses = []
            for course in course_list.all():
                serialized_courses.append(
                    serialize_course(course)
                )
            return serialized_courses

        def serialize_profile(user_profile):
            """
            Serializes an user profile object.
            :param user_profile: user profile object
            :return: dictionary with the user profile info
            """
            return {
                'bio': user_profile.bio,
                'description': user_profile.description,
                'resume': user_profile.resume,
                'birth_date': user_profile.birth_date.strftime("%d-%m-%Y")
            }

        def serialize_course(course_status_object):
            return {
                'title': course_status_object.course.title,
                'url': course_status_object.course.url,
                'badge': course_status_object.course.badge,
                'provider': course_status_object.course.provider.name
            }

        collection_db = MongoClient().resumme.profiles
        for user in User.objects.all():
            try:
                data = {}
                data['profile'] = serialize_profile(
                    Bio.objects.get(user=user)
                )

                data['courses'] = serialize_user_provider_profiles(
                    ProviderProfile.objects.filter(user=user)
                )
                collection_db.update_one({"_id": user.username},
                                         {"$set": data},
                                         upsert=True)

            except Exception as e:
                raise CommandError('Error in request {}'.format(e))
