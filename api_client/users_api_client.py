import requests

from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints
from data_models.users_api_client import UserDataModel
from exceptions.users_api_client import InvalidUserDataModelDict
from data_provider.users_api_client import PostUserDataProvider, PutUserDataProvider
from wrappers.api_clients import api_token_wrapper
from wrappers.api_clients import attach_allure_data_wrapper
from allure import step


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"
    _POST_DATA = PostUserDataProvider.get_post_user_datamodel().__next__()
    _PUT_DATA = PutUserDataProvider.get_put_user_datamodel().__next__()

    @api_token_wrapper
    def get(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    @api_token_wrapper
    def post(self, data):
        endpoint = UsersEndpoints.build_post_users_endpoint()
        self.logger.debug(f"Validating payload {data} format be corrent")
        for key in data.keys():
            self.logger.debug(f"{key} is validated!")
            if not key in UserDataModel.request_post_user_keys:
                self.logger.error(f"{key} is wrong key in request!")
                raise InvalidUserDataModelDict("Wrong data format provided!")

        return self._post(endpoint=endpoint, data=data)

    @api_token_wrapper
    def put(self, user_id: int, data):
        endpoint = UsersEndpoints.build_put_users_endpoint(user_id=user_id)

        return self._put(endpoint=endpoint, data=data)

    def delete(self, user_id: int):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._delete(endpoint=endpoint)

    @step("Create a user")
    def create_user(self, data: dict = _POST_DATA):
        self.logger.debug(f"Creating a user..")
        self.logger.debug(f"Sending POST request with payload - {data}")
        return self.post(data=data)

    @step("Get a user")
    @attach_allure_data_wrapper
    def find_user(self, user_id: int):
        self.logger.debug(f"Searching for user by user_id - {user_id}..")
        self.logger.debug(f"Sending GET request..")
        return self.get(user_id=user_id)

    @step("Edit a user")
    def edit_user(self, user_id: int, data: dict = _PUT_DATA):
        self.logger.debug(f"Editing user by user_id - {user_id}..")
        self.logger.debug(f"Sending PUT request..")
        return self.put(user_id=user_id, data=data)

    @step("Delete a user")
    def delete_user(self, user_id: int):
        self.logger.debug(f"Deleting user by user_id - {user_id}..")
        self.logger.debug(f"Sending DELETE request..")
        return self.delete(user_id=user_id)

    def retrieve_users(self):
        endpoint = UsersEndpoints.build_retrieve_users_endpoint()

        return self._retrieve(endpoint=endpoint)
