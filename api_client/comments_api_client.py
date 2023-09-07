from api_client.base_api_client import BaseApiClient
from helpers.comments_api_client import CommentsEndpoint


class CommentsApiClient(BaseApiClient):
    ENDPOINT = "/comments"

    def __init__(self, api_token=None):
        if api_token:
            super().__init__(api_token=api_token)

    def get(self, user_id):
        endpoint = CommentsEndpoint.build_getdel_post_endpoint(user_id=user_id)
        return self.__client.get(endpoint=endpoint)

    def delete(self, user_id):
        endpoint = CommentsEndpoint.build_getdel_post_endpoint(user_id=user_id)
        return self.__client.delete(endpoint=endpoint)
