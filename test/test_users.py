from access.api_token import API_TOKEN


class TestUsersCRUD:
    _USER_POST: dict = None
    _USER_PUT: dict = None

    def test_create_user(self, users_client):
        users_client.set_api_token(api_token=API_TOKEN)
        response = users_client.create_user()
        self.__class__._USER_POST = response.json()  # save created user json data in class dict variable
        assert response.ok, f"Failed to create user, status code {response}"

    def test_get_user(self, users_client):
        response = users_client.find_user(user_id=self._USER_POST["id"])
        assert response.ok, f"Failed get user by userid={self._USER_POST['id']}, {response.json()}"

    def test_put_user(self, users_client):
        response = users_client.edit_user(user_id=self._USER_POST["id"])
        self.__class__._USER_PUT = response.json()  # save user json data in class dict variable after put request
        assert self._USER_POST['id'] == self._USER_PUT['id']
        assert response.ok, f"Failed get user by userid={self._USER_POST['id']}, {response.json()}"
        assert not self._USER_PUT == self._USER_POST, f"User post : {self._USER_POST}, user put: {self._USER_PUT} seems are equal ;/"

    def test_delete_user(self, users_client):
        response = users_client.delete_user(user_id=self._USER_POST["id"])
        assert response.ok, f"Failed to delete user by userid={self._USER_POST['id']}, {response.json()}"
        assert not users_client.get(user_id=self._USER_POST).ok, f"User still exist by user_id {self._USER_POST['id']}"
