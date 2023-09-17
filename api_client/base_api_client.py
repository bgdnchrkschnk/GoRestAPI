import requests
from random import randint

from exceptions.base_api_client import *


class BaseApiClient:
    BASE_URL = "https://gorest.co.in/public/v2"

    def __init__(self, logger, api_token=None):
        self.__client = requests.Session()
        self.__api_token = api_token if api_token else None
        self._headers_update()
        self.__logger = logger

    @property
    def logger(self):
        return self.__logger

    @property
    def api_token(self):
        return self.__api_token

    @api_token.setter
    def api_token(self, api_token):
        self.__api_token = api_token
        self._headers_update()

    def _headers_update(self):
        header = f"Bearer {self.api_token}"
        headers = dict(Authorization=header)
        self.__client.headers.update(headers)

    def _get(self, endpoint):
        return self.__client.get(url=endpoint)

    def _post(self, endpoint, data):
        return self.__client.post(url=endpoint, json=data)

    def _put(self, endpoint, data):
        return self.__client.put(url=endpoint, json=data)

    def _delete(self, endpoint):
        return self.__client.delete(url=endpoint)

    def _retrieve(self, endpoint):
        return self.__client.get(url=endpoint)

    def set_api_token(self, api_token):
        self.api_token = api_token

    def get_random_post_id(self, response_obj):
        return response_obj.json()[randint(0,len(response_obj.json()))]["id"]


