import requests


class BaseApiClient:
    BASE_URL = "https://gorest.co.in/public/v2"

    def __init__(self, api_token=None):
        self.__client = requests.Session()
        if api_token:
            self.__api_token = api_token

    def __headers_update(self):
        header = f"Bearer {self.__api_token}"
        self.__client.headers.update(dict(Autorization=header))

    def _get(self, endpoint):
        return self.__client.get(url=endpoint)

    def _post(self, endpoint, data):
        return self.__client.post(url=endpoint, json=data)

    def _put(self, endpoint, data):
        return self.__client.put(url=endpoint, json=data)

    def _delete(self, endpoint):
        return self.__client.delete(url=endpoint)
