from api_client.base_api_client import BaseApiClient


class PostsEndpoint:

    @staticmethod
    def build_getpost_post_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        from api_client.posts_api_client import PostsApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id) + PostsApiClient.ENDPOINT
        return endpoint

    @staticmethod
    def build_retrieve_posts_endpoint():
        from api_client.posts_api_client import PostsApiClient
        endpoint = BaseApiClient.BASE_URL + PostsApiClient.ENDPOINT
        return endpoint
