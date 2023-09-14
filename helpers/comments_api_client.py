from api_client.base_api_client import BaseApiClient


class CommentsEndpoint:

    @staticmethod
    def build_getpost_comment_endpoint(post_id):
        from api_client.posts_api_client import PostsApiClient
        from api_client.comments_api_client import CommentsApiClient
        endpoint = BaseApiClient.BASE_URL + PostsApiClient.ENDPOINT + str(post_id) + CommentsApiClient.ENDPOINT
        return endpoint

    @staticmethod
    def build_retrieve_comments_endpoint():
        from api_client.comments_api_client import CommentsApiClient
        endpoint = BaseApiClient.BASE_URL + CommentsApiClient.ENDPOINT
        return endpoint

