# import pytest

class TestUsersCRUD:

    def test_create_user(self, users_client):
        # users_client.set_api_token("309655f52aa1dd3eb0f6be507193717e57833e81c35cd665e44af77aaf098e75")
        response = users_client.get(user_id=5133765)
        print(response.json())
        assert response.ok, response.json()

