from api_client.base_api_client import BaseApiClient
from helpers.posts_api_client import PostsEndpoint


class PostsApiClient(BaseApiClient):
    ENDPOINT = "/posts"

    def get(self, user_id):
        endpoint = PostsEndpoint.build_getdel_post_endpoint(user_id=user_id)
        return self.__client.get(endpoint=endpoint)

    def delete(self, user_id):
        endpoint = PostsEndpoint.build_getdel_post_endpoint(user_id=user_id)
        return self.__client.delete(endpoint=endpoint)
