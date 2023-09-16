from api_client.base_api_client import BaseApiClient
from helpers.posts_api_client import PostsEndpoint
from data_provider.posts_api_client import UserPostDataProvider
from data_models.posts_api_client import PostDataModel
from exceptions.posts_api_client import InvalidUserDataModelDict
from allure import step


class PostsApiClient(BaseApiClient):
    ENDPOINT = "/posts/"

    def get(self, user_id):
        endpoint = PostsEndpoint.build_getpost_post_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, user_id: int, data: dict = None):
        endpoint = PostsEndpoint.build_getpost_post_endpoint(user_id=user_id)
        if not data:
            data = self._get_user_post_model_for_post()
        else:
            count = 0
            for key in data:
                if key in PostDataModel.request_users_post_keys:
                    count += 1
                else:
                    raise InvalidUserDataModelDict("Wrong data format provided!")
        return self._post(endpoint=endpoint, data=data)


    @staticmethod
    def _get_user_post_model_for_post():
        return UserPostDataProvider.get_user_post_datamodel()

    @step("Create a user post")
    def create_post(self, user_id: int, data: dict = None):
        return self.post(user_id=user_id, data=data)

    @step("Get a user post")
    def find_user_posts(self, user_id: int):
        return self.get(user_id=user_id)

    def retrieve_posts(self):
        endpoint = PostsEndpoint.build_retrieve_posts_endpoint()
        return self._retrieve(endpoint=endpoint)