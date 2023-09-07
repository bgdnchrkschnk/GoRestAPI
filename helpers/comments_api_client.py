from api_client.base_api_client import BaseApiClient


class CommentsEndpoint:

    @staticmethod
    def build_getdel_post_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        from api_client.comments_api_client import CommentsApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + user_id + CommentsApiClient.ENDPOINT
        return endpoint
