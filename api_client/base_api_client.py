import requests

from exceptions.base_api_client import *

class BaseApiClient:
    BASE_URL = "https://gorest.co.in/public/v2"

    def __init__(self, api_token=None):
        self.__client = requests.Session()
        if api_token:
            self.__api_token = api_token
            self._headers_update()

    def _headers_update(self):
        header = f"Bearer {self.__api_token}"
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

