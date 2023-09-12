import requests

from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints
from data_models.users_api_client import *
from exceptions.users_api_client import InvalidUserDataModelDict
from data_provider.users_api_client import PostUserDataProvider, PutUserDataProvider
from wrappers.api_clients import *


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"

    def __init__(self, api_token=None):
        super().__init__(api_token)
        self.__id_ = None
        self.__email_ = None

    @api_token_wrapper
    def get(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    @api_token_wrapper
    def post(self, data: dict = None):
        endpoint = UsersEndpoints.build_post_users_endpoint()
        if not data:
            data = self._get_user_model_for_post()
            if not len(data):
                data = self._get_user_model_for_post()
        else:
            count = 0
            for key in data:
                if key in post_user_keys:
                    count += 1
            if not count == len(post_user_keys):
                raise InvalidUserDataModelDict("Wrong data format provided!")
        self.__email_ = data["email"]
        return self._post(endpoint=endpoint, data=data)

    @api_token_wrapper
    def put(self, user_id: int, data: dict = None):
        endpoint = UsersEndpoints.build_put_users_endpoint(user_id=user_id)
        if not data:
            data = self._get_user_model_for_put()
        else:
            count = 0
            for key in data:
                if key in put_user_keys:
                    count += 1
            if not count == len(put_user_keys):
                raise InvalidUserDataModelDict("Wrong data format provided!")
        return self._put(endpoint=endpoint, data=data)

    def delete(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._delete(endpoint=endpoint)

    @staticmethod
    def _get_user_model_for_post():
        user_dict = PostUserDataProvider.get_post_user_datamodel()
        return user_dict

    @staticmethod
    def _get_user_model_for_put():
        user_dict = PutUserDataProvider.get_put_user_datamodel()
        return user_dict

    def create_user(self, data: dict = None):
        return self.post(data=data)

    def find_user(self, user_id: int):
        return self.get(user_id=user_id)

    def edit_user(self, user_id: int, data: dict = None):
        return self.put(user_id=user_id, data=data)

    def delete_user(self, user_id: int):
        return self.delete(user_id=user_id)
