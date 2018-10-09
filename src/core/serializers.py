from core.models import CourseStatus

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
            course_list=courses.filter(status="c").all()
        )
        course_list['in_progress'] = serialize_course_list(
            course_list=courses.filter(status="i").all()
        )
    return course_list

def courses_from_username(username: str) -> dict:
    courses = {'all': []}
    courses_status = CourseStatus.objects.filter(profile__user__username=username)
    for cs in courses_status:
        serialized_course = serialize_course_from_course_provider(cs)
        courses['all'] += [serialized_course]
        for t in cs.course.tags.all():
            tag_name = t.name
            if not tag_name in courses:
                courses[tag_name] = []
            courses[tag_name] += [serialized_course]
    return courses


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
        'full_name': user_profile.full_name,
        'mail': user_profile.mail,
        'birth_date': user_profile.birth_date.strftime("%d-%m-%Y"),
        'avatar': user_profile.avatar,
    }


def serialize_course(course_status_object):
    return {
        'title': course_status_object.course.title,
        'url': course_status_object.course.url,
        'badge': course_status_object.course.badge,
        'provider': course_status_object.course.provider.name
    }

def serialize_course_from_course_provider(course_status_object):
    return {
        'title': course_status_object.course.title,
        'url': course_status_object.course.url,
        'badge': course_status_object.course.badge,
        'provider': course_status_object.course.provider.name
    }

def serialize_timeline_item(timeline_object):
    return {
        'type': timeline_object.type,
        'title': timeline_object.title,
        'description': timeline_object.description,
        'start_date': timeline_object.start_date,
        'end_date': timeline_object.end_date,
    }
