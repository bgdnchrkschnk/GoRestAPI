import pytest_check as check


class TestTodosCRUD:
    _USER_ID = None

    def test_create_user_todo(self, users_client, todos_client):
        response = users_client.create_user()
        self.__class__._USER_ID = response.json()["id"]
        todos_client.

