from api_client.base_api_client import BaseApiClient
from helpers.comments_api_client import CommentsEndpoint
from data_provider.comments_api_client import PostCommentDataProvider
from data_models.comments_api_client import *
from exceptions.comments_api_client import *


class CommentsApiClient(BaseApiClient):
    ENDPOINT = "/comments"

    # def get(self, user_id):
    #     endpoint = CommentsEndpoint.build_getpost_comment_endpoint(user_id=user_id)
    #     return self.__client.get(endpoint=endpoint)

    def post(self, post_id: int, data: dict = None):
        endpoint = CommentsEndpoint.build_getpost_comment_endpoint(post_id=post_id)
        if not data:
            data = self._get_post_comment_model_for_post()
        else:
            count = 0
            for key in data:
                if key in post_comment_keys:
                    count += 1
            if not count == len(post_comment_keys):
                raise InvalidUserDataModelDict("Wrong data format provided!")
        return self._post(endpoint=endpoint, data=data)

    @staticmethod
    def _get_post_comment_model_for_post():
        return PostCommentDataProvider.get_post_comment_datamodel()


