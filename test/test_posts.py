import pytest_check as check
from data_models.posts_api_client import PostDataModel
from allure import title, description, severity, severity_level, suite

@suite("Users posts CRUD")
class TestPostsCRUD:
    _USER_ID: int = None

    @title("Check user post creates successfully")
    @description("Test verifies if user post successfully created with POST request")
    @severity(severity_level.CRITICAL)
    def test_create_post(self, users_client, posts_client):
        response = users_client.create_user()
        self.__class__._USER_ID = int(response.json()['id'])
        user_id = self.__class__._USER_ID
        response = posts_client.create_post(user_id=user_id)

        check.is_true(response.ok, f"{response.status_code} Failed to create user post, {response.json()}")
        [check.is_true(key in PostDataModel.response_users_post_keys) for key in response.json().keys()]

    @title("Check user post gets successfully")
    @description("Test verifies if user post successfully get from server with GET request")
    @severity(severity_level.CRITICAL)
    def test_get_user_post(self, posts_client):
        response = posts_client.find_user_posts(user_id=self.__class__._USER_ID)
        expected_id = self.__class__._USER_ID
        actual_id = response.json()[0]["user_id"]

        check.is_true(response.ok, f"{response.status_code} Failed to get user post, {response.json()}")
        check.equal(expected_id, actual_id, f"Expected id {expected_id} is not equal to actual id {actual_id}")
