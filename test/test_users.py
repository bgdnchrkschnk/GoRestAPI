from data_models.users_api_client import UserDataModel
import pytest_check as check
from allure import title, description, severity, severity_level, suite, attach, attachment_type

@suite("Users CRUD")
class TestUsersCRUD:
    _USER_POST: dict = None
    _USER_PUT: dict = None

    @title("Check user creates successfully")
    @description("Test verifies if user successfully created with POST request")
    @severity(severity_level.CRITICAL)
    def test_create_user(self, users_client):
        response = users_client.create_user()
        self.__class__._USER_POST = response.json()  # save created user json data in class dict variable

        check.is_true(response.ok, f"Failed to create user, status code {response}")
        [check.is_true(key in UserDataModel.response_post_user_keys) for key in self.__class__._USER_POST.keys()]

    @title("Check get user successfully")
    @description("Test verifies get user is correct with GET request")
    @severity(severity_level.CRITICAL)
    def test_get_user(self, users_client):
        response = users_client.find_user(user_id=self._USER_POST["id"])

        check.is_true(response.ok, f"Failed get user by userid={self._USER_POST['id']}, {response.json()}")


    @title("Check user edits on server successfully")
    @description("Test verifies if user successfully edited with PUT request")
    @severity(severity_level.CRITICAL)
    def test_put_user(self, users_client):
        response = users_client.edit_user(user_id=self._USER_POST["id"])
        self.__class__._USER_PUT = response.json()  # save user json data in class dict variable after put request

        check.is_true(self._USER_POST['id'] == self._USER_PUT['id'])
        check.is_true(response.ok, f"Failed get user by userid={self._USER_POST['id']}, {response.json()}")
        check.not_equal(self._USER_PUT, self._USER_POST, f"User post : {self._USER_POST}, user put: {self._USER_PUT} seems are equal ;/")


    @title("Check user deleted successfully")
    @description("Test verifies if user successfully deleted with DELETE request")
    @severity(severity_level.CRITICAL)
    def test_delete_user(self, users_client):
        response = users_client.delete_user(user_id=self._USER_POST["id"])

        check.is_not(response.ok, f"Failed to delete user by userid={self._USER_POST['id']}")
        check.is_not(users_client.get(user_id=self._USER_POST).ok, f"User still exist by user_id {self._USER_POST['id']}")
