import pytest_check as check
from data_models.comments_api_client import CommentDataModel
from allure import title, description, severity, severity_level, suite

@suite("Post comments CRUD")
class TestCommentsCRUD:
    _USER_ID = None
    _POST_ID = None

    @title("Check post comment creates successfully")
    @description("Test verifies if post comment successfully created with POST request")
    @severity(severity_level.CRITICAL)
    def test_create_post_comment(self, users_client, posts_client, comments_client):
        response = users_client.create_user()
        self.__class__._USER_ID = response.json()["id"]
        response = posts_client.create_post(user_id=self.__class__._USER_ID)
        self.__class__._POST_ID = response.json()["id"]
        response = comments_client.create_post_comment(post_id=self.__class__._POST_ID)

        check.is_true(response.ok, f"Failed to create a comment for post_id {self.__class__._POST_ID}")
        [check.is_true(key in CommentDataModel.response_post_comment_keys) for key in response.json().keys()]

    @title("Check post comment get is successfull with GET response")
    @description("Test verifies if post comment successfully created with POST request")
    @severity(severity_level.CRITICAL)
    def test_get_post_comments(self, comments_client):
        response = comments_client.find_post_comments(post_id=self.__class__._POST_ID)

        check.is_true(response.ok, f"Failed to fetch post comments by post_id {self.__class__._POST_ID}")
        [check.is_true(key in response.json()[0].keys()) for key in CommentDataModel.response_post_comment_keys]



