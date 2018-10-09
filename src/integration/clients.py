from .mixins import (IntegrationMixin, JsonResponseIntegrationMixin,
                     HtmlResponseIntegrationMixin)

class TreehouseIntegration(JsonResponseIntegrationMixin, IntegrationMixin):
    integration_url = 'https://www.teamtreehouse.com/{username}.json'

    @staticmethod
    def parse_provider_badge_courses(badge_node):
        parsed_courses = []

        for course in badge_node['courses']:
            parsed_courses.append({
                'title': course['title'],
                'url': course['url'],
                'badge': badge_node['icon_url'],
                'provider': 'treehouse'
            })

        return parsed_courses

    def parse_data_to_model(self, provider_response):
        courses = []
        for badge in provider_response['badges']:
            parsed_courses = self.parse_provider_badge_courses(badge)
            if parsed_courses:
                courses += parsed_courses
        return courses

class SoloLearnIntegration(HtmlResponseIntegrationMixin, IntegrationMixin):
    base_url = 'https://www.sololearn.com'
    integration_url = '/'.join([base_url, 'Profile/{username}'])
    course_url = '/'.join([base_url, 'Play/{course_name}'])

    def parse_html_object(self, html_node):
        course_profile_url = html_node.attrs['href']
        course_name = course_profile_url.split('/')[-1]
        return {
            'title': html_node.img.attrs['alt'],
            'url': self.course_url.format(course_name=course_name),
            'badge': self.base_url + html_node.img.attrs['src'],
            'provider': 'sololearn',
        }

    def parse_data_to_model(self, provider_response):
        html_courses = provider_response.findAll("a", {"class": "course"})
        return [self.parse_html_object(course) for course in html_courses]
