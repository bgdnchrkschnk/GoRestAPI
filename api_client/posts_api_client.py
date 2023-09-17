from api_client.base_api_client import BaseApiClient
from helpers.posts_api_client import PostsEndpoint
from data_provider.posts_api_client import UserPostDataProvider
from data_models.posts_api_client import PostDataModel
from exceptions.posts_api_client import InvalidUserDataModelDict
from allure import step
from wrappers.api_clients import attach_allure_data_wrapper


class PostsApiClient(BaseApiClient):
    ENDPOINT = "/posts/"
    _POST_DATA = UserPostDataProvider.get_user_post_datamodel().__next__()

    def get(self, user_id):
        endpoint = PostsEndpoint.build_getpost_post_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, user_id: int, data):
        endpoint = PostsEndpoint.build_getpost_post_endpoint(user_id=user_id)

        for key in data:
            if not key in PostDataModel.request_users_post_keys:
                raise InvalidUserDataModelDict("Wrong data format provided!")

        return self._post(endpoint=endpoint, data=data)

    @step("Create a user post")
    def create_post(self, user_id: int, data: dict = _POST_DATA):
        return self.post(user_id=user_id, data=data)

    @step("Get a user post")
    @attach_allure_data_wrapper
    def find_user_posts(self, user_id: int):
        return self.get(user_id=user_id)

    def retrieve_posts(self):
        endpoint = PostsEndpoint.build_retrieve_posts_endpoint()
        return self._retrieve(endpoint=endpoint)