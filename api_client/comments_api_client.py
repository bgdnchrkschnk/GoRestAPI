from api_client.base_api_client import BaseApiClient
from data_provider.comments_api_client import PostCommentDataProvider
from data_models.comments_api_client import CommentDataModel
from exceptions.comments_api_client import *
from allure import step

from wrappers.api_clients import attach_allure_data_wrapper


class CommentsApiClient(BaseApiClient):
    ENDPOINT = "/comments/"
    _POST_DATA = PostCommentDataProvider.get_post_comment_datamodel().__next__()

    def get(self, post_id):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_getpost_comment_endpoint(post_id=post_id)
        return self._get(endpoint=endpoint)

    def post(self, post_id: int, data):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_getpost_comment_endpoint(post_id=post_id)

        for key in data:
            if not key in CommentDataModel.request_post_comment_keys:
                raise InvalidUserDataModelDict("Wrong data format provided!")

        return self._post(endpoint=endpoint, data=data)


    @step("Create a comment for a post")
    def create_post_comment(self, post_id: int, data: dict = _POST_DATA):
        self.logger.debug(f"Creating user post comment by post_id {post_id}")
        self.logger.debug("Sending POST request..")
        return self.post(post_id=post_id, data=data)

    @step("Get post comments")
    @attach_allure_data_wrapper
    def find_post_comments(self, post_id):
        self.logger.debug(f"Getting user post comments by post_id {post_id}")
        self.logger.debug("Sending GET request..")
        return self.get(post_id=post_id)

    def retrieve_comments(self):
        from helpers.comments_api_client import CommentsEndpoint
        endpoint = CommentsEndpoint.build_retrieve_comments_endpoint()
        return self._retrieve(endpoint=endpoint)



