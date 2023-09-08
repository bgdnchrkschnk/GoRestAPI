from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints
from data_models.users_api_client import *
from exceptions.users_api_client import InvalidUserDataModelDict
from data_provider.users_api_client import PostUserDataProvider, PutUserDataProvider


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"

    def __init__(self, api_token=None):
        if api_token:
            super().__init__(api_token=api_token)

    @property
    def api_token(self):
        return self.__api_token if self.__api_token else None

    def get(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, data: dict = None):
        endpoint = UsersEndpoints.build_post_users_endpoint()
        if not data:
            data = self._get_user_model_for_post()
        else:
            data = asdict(PostUserModel(data))
        return self._post(endpoint=endpoint, data=data)

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

    def set_api_token(self, api_token):
        super().__init__(api_token=api_token)




a = UserApiClient()
a.set_api_token("bhebjc")