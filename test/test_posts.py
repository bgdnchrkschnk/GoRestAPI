from access.api_token import API_TOKEN
import pytest_check as check


class TestPostsCRUD:
    _USER_ID: int = None

    def test_create_post(self, users_client, posts_client):
        users_client.set_api_token(api_token=API_TOKEN)
        posts_client.set_api_token(api_token=API_TOKEN)
        response = users_client.create_user()
        self.__class__._USER_ID = int(response.json()['id'])  # save user_id of created user
        user_id = self.__class__._USER_ID
        response = posts_client.create_post(user_id=user_id)
        check.is_true(response.ok, f"{response.status_code} Failed to create user post, {response.json()}")

    def test_get_user_post(self, posts_client):
        posts_client.set_api_token(api_token=API_TOKEN)
        response = posts_client.find_user_posts(user_id=self.__class__._USER_ID)
        expected_id = self.__class__._USER_ID
        actual_id = response.json()[0]["user_id"]
        check.is_true(response.ok, f"{response.status_code} Failed to get user post, {response.json()}")
        check.equal(expected_id, actual_id, f"Expected id {expected_id} is not equal to actual id {actual_id}")
