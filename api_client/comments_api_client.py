from api_client.base_api_client import BaseApiClient
from data_provider.comments_api_client import PostCommentDataProvider
from data_models.comments_api_client import CommentDataModel
from exceptions.comments_api_client import *
from allure import step


class CommentsApiClient(BaseApiClient):
    ENDPOINT = "/comments/"

    def get(self, post_id):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_getpost_comment_endpoint(post_id=post_id)
        return self._get(endpoint=endpoint)

    def post(self, post_id: int, data: dict = None):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_getpost_comment_endpoint(post_id=post_id)
        if not data:
            data = self._get_post_comment_model_for_post()
        else:
            count = 0
            for key in data:
                if key in CommentDataModel.request_post_comment_keys:
                    count += 1
                else:
                    raise InvalidUserDataModelDict("Wrong data format provided!")
        return self._post(endpoint=endpoint, data=data)

    @staticmethod
    def _get_post_comment_model_for_post():
        return PostCommentDataProvider.get_post_comment_datamodel()

    @step("Create a comment for a post")
    def create_post_comment(self, post_id: int, data: dict = None):
        return self.post(post_id=post_id, data=data)

    @step("Get post comments")
    def find_post_comments(self, post_id):
        return self.get(post_id=post_id)

    def retrieve_comments(self):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_retrieve_comments_endpoint()
        return self._retrieve(endpoint=endpoint)



