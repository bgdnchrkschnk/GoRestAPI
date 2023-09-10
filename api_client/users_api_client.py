import requests

from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints
from data_models.users_api_client import *
from exceptions.users_api_client import InvalidUserDataModelDict
from data_provider.users_api_client import PostUserDataProvider, PutUserDataProvider
from wrappers.api_clients import *


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"

    @api_token_wrapper
    def get(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    @api_token_wrapper
    def post(self, data: dict = None):
        endpoint = UsersEndpoints.build_post_users_endpoint()
        if not data:
            data = self._get_user_model_for_post()
        else:
            try:
                data = asdict(PostUserModel(data))
            except:
                raise InvalidUserDataModelDict("Wrong data format provided!")
        return self._post(endpoint=endpoint, data=data)

    @api_token_wrapper
    def put(self, userid: int, data: dict = None):
        endpoint = UsersEndpoints.build_put_users_endpoint(user_id=userid)
        if not data:
            data = self._get_user_model_for_put()
        else:
            data = asdict(PostUserModel(data))
        return self._post(endpoint=endpoint, data=data)

    def delete(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._delete(endpoint=endpoint)

    def _get_user_model_for_post(self):
        user_dict = PostUserDataProvider.get_post_user_datamodel()
        return user_dict

    def _get_user_model_for_put(self):
        user_dict = PutUserDataProvider.get_put_user_datamodel()
        return user_dict


