from access.api_token import API_TOKEN

class TestPostsCRUD:
    _POST_POST: dict = None
    _POST_PUT: dict = None

    def test_create(self, users_client, posts_client):

