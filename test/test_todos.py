import pytest_check as check
from data_models.todos_api_client import TodoDataModel
from allure import suite, title, description, severity, severity_level

@suite("User Todos CRUD")
class TestTodosCRUD:
    _USER_ID = None

    @title("Check user todo creates successfully")
    @description("Test verifies if user todo created successfully with POST request")
    @severity(severity_level.CRITICAL)
    def test_create_user_todo(self, users_client, todos_client):
        response = users_client.create_user()
        self.__class__._USER_ID = int(response.json()["id"])
        response = todos_client.create_todo(user_id=self.__class__._USER_ID)

        check.is_true(response.ok, f"Unsuccessful creating user todo, status code {response.status_code}")
        [check.is_true(key in response.json()) for key in TodoDataModel.response_user_todo_keys]

    @title("Check get existing users todo successfully")
    @description("Test verifies if user todos fetched successfully with get request")
    @severity(severity_level.CRITICAL)
    def test_find_user_todo(self, todos_client):
        response = todos_client.find_todo(user_id=self._USER_ID)
        expected_user_id = self.__class__._USER_ID
        actual_user_id = response.json()[0]['user_id']

        check.is_true(response.ok, f"Failded to get users todos by user_id {self.__class__._USER_ID}")
        check.is_true(actual_user_id == expected_user_id, f"Expected user id does not equal to actual!")
        [check.is_true(key in response.json()[0].keys()) for key in TodoDataModel.response_user_todo_keys]



