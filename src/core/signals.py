from django.contrib.auth.models import User
from .models import ProviderProfile, Provider, Course, UserProfile, CourseStatus
from integration.clients import TreehouseIntegration, SoloLearnIntegration
from integration.exceptions import ProviderRequestError

from django.db.models.signals import post_save
import gevent

def update_user_when_auth(sender, instance, **kwargs):
    gevent.spawn(update_db_data, instance)

def update_user_when_provider_profile_updated(sender, instance, **kwargs):
    gevent.spawn(update_db_data, instance.user)

def update_db_data(user_instance):
    def set_provider_profiles(user_instance):
        for provider in Provider.objects.all():
            ProviderProfile.objects.get_or_create(user=user_instance, provider=provider)

    def init_user_bio(user_instance):
        empty_bio, created = UserProfile.objects.get_or_create(user=user_instance)

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
        'treehouse': TreehouseIntegration(),
        'sololearn': SoloLearnIntegration(),
    }

    for provider_profile in ProviderProfile.objects.filter(user=user_instance, provider__enabled=True):
        try:
            provider_name = provider_profile.provider.name
            provider_nickname = provider_profile.username_provider
            course_list = provider_client[provider_name].retrieve_data(username=provider_nickname)
            add_courses_to_user(provider_profile=provider_profile,
                                course_list=course_list)
        except ProviderRequestError as e:
            pass


post_save.connect(update_user_when_auth,
                  sender=User,
                  dispatch_uid="user_profile_modified")

post_save.connect(update_user_when_provider_profile_updated,
                  sender=ProviderProfile,
                  dispatch_uid="provider_profile_modified")
