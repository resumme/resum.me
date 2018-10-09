import requests
from bs4 import BeautifulSoup

from .exceptions import ProviderRequestError, ProviderUrlNotDefined

class JsonResponseIntegrationMixin(object):
    def get_data_from_provider(self, username):
        if not self.integration_url:
            raise ProviderUrlNotDefined('Integration url is not defined')
        response = requests.get(self.integration_url.format(username=username))
        if not response.ok:
            raise ProviderRequestError('Could not fetch the data with the provider')
        return response.json()

class HtmlResponseIntegrationMixin(object):
    def get_data_from_provider(self, username):
        if not self.integration_url:
            raise ProviderUrlNotDefined('Integration url is not defined')
        req = requests.get(self.integration_url.format(username=username))
        soup = BeautifulSoup(req.text, "lxml")
        return soup


class IntegrationMixin(object):
    def parse_data_to_model(self, provider_response):
        raise NotImplementedError()

    def retrieve_data(self, username):
        provider_response = self.get_data_from_provider(username)
        serialized_data = self.parse_data_to_model(provider_response)
        return serialized_data
