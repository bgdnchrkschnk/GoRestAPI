from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints
from data_models.users_api_client import *
from exceptions.users_api_client import InvalidUserDataModelDict


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"

    def __init__(self, api_token=None):
        if api_token:
            super().__init__(api_token=api_token)

    def get(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, data: PostUserModel):
        endpoint = UsersEndpoints.build_post_users_endpoint()
        return self._post(endpoint=endpoint, data=asdict(data))

    def put(self, userid: int, data: PostUserModel):
        endpoint = UsersEndpoints.build_put_users_endpoint(user_id=userid)
        return self._post(endpoint=endpoint, data=asdict(data))

    def delete(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._delete(endpoint=endpoint)

    @staticmethod
    def __get_user_model_for_post(user_dict: dict):
        try:
            return PostUserModel(name=user_dict["name"],
                                 gender=user_dict["gender"],
                                 email=user_dict["email"],
                                 status=user_dict["status"])
        except:
            raise InvalidUserDataModelDict(f"Provided dict data provided!")

    @staticmethod
    def __get_user_model_for_put(user_dict: dict):
        try:
            return PutUserModel(name=user_dict["name"],
                                email=user_dict["email"],
                                status=user_dict["status"])
        except:
            raise InvalidUserDataModelDict(f"Provided dict data provided!")
