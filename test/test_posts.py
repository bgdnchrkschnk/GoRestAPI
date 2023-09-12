from access.api_token import API_TOKEN


class TestPostsCRUD:
    _POST_POST: dict = None
    _POST_PUT: dict = None
    _USER_ID: int = None

    def test_create_post(self, users_client, posts_client):
        users_client.set_api_token(api_token=API_TOKEN)
        posts_client.set_api_token(api_token=API_TOKEN)
        response = users_client.create_user()
        user_id = int(response.json()['id'])
        response = posts_client.create_post(user_id=user_id)
        print(response.json())
        assert response.ok, f"Failed to create user post, {response.json()}"
