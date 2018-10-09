from django.core.management.base import BaseCommand, CommandError
from integration.clients import TreehouseIntegration, SoloLearnIntegration
from django.contrib.auth.models import User
from core.models import ProviderProfile, Provider, Course, Bio, CourseStatus

class Command(BaseCommand):
    help = 'Test BeautifulSoup integration arquitecture'

    def handle(self, *args, **options):
        treehouse_client = TreehouseIntegration()
        solo_learn_client = SoloLearnIntegration()
        user_instance = User.objects.get(username='adriancast')
        try:
            def set_provider_profiles(user_instance):
                for provider in Provider.objects.all():
                    ProviderProfile.objects.get_or_create(user=user_instance, provider=provider)

            def init_user_bio(user_instance):
                empty_bio, created = Bio.objects.get_or_create(user=user_instance)

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

            def add_courses_to_user(provider_profile, course_list):
                for course in course_list:
                    new_course, created = Course.objects.get_or_create(
                        title=course['title'],
                        url=course['url'],
                        badge=course['badge'],
                        provider=provider_profile.provider
                    )
                    manage_relation_course_profile(provider_profile, new_course, 'c')

            init_user_bio(user_instance=user_instance)

            set_provider_profiles(user_instance=user_instance)

            provider_client = {
                'treehouse': treehouse_client,
                'sololearn': solo_learn_client,
            }

            for provider_profile in ProviderProfile.objects.filter(user=user_instance):
                provider_name = provider_profile.provider.name
                provider_nickname = provider_profile.username_provider
                course_list = provider_client[provider_name].retrieve_data(username=provider_nickname)
                add_courses_to_user(provider_profile=provider_profile,
                                    course_list=course_list)

        except Exception as e:
            raise CommandError('Error in request {}'.format(e))
