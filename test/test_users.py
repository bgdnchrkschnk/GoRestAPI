# import pytest
import access.api_token


class TestUsersCRUD:

    def test_create_user(self, users_client):
        users_client.set_api_token("819e69004d2ea659faf886ece1355d4994f2b390ba9b76253a01dfbe3d02980b")
        response = users_client.get(user_id=5133765)
        print(response.json())
        assert response.ok, response.json()

