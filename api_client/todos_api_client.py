from api_client.base_api_client import BaseApiClient
from data_provider.todos_api_client import TodosDataProvider
from data_models.todos_api_client import TodoDataModel
from exceptions.todos_api_client import InvalidUserTodoDataModelDict
from allure import step
from wrappers.api_clients import attach_allure_data_wrapper


class TodosApiClient(BaseApiClient):
    ENDPOINT = "/todos/"
    POST_DATA = TodosDataProvider.get_post_todo_datamodel().__next__()

    def get(self, user_id):
        from helpers.todos_api_client import TodosEndpoint
        endpoint = TodosEndpoint.build_getpost_todos_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, user_id, data):
        from helpers.todos_api_client import TodosEndpoint
        endpoint = TodosEndpoint.build_getpost_todos_endpoint(user_id=user_id)

        for key in data.keys():
            if not key in TodoDataModel.request_user_todo_keys:
                raise InvalidUserTodoDataModelDict("Wrong data format provided!")

        return self._post(endpoint=endpoint, data=data)

    def retrieve_todos(self):
        from helpers.todos_api_client import TodosEndpoint
        return self._retrieve(endpoint=TodosEndpoint.build_retrieve_todos_endpoint())

    @step("Get user todos")
    @attach_allure_data_wrapper
    def find_todo(self, user_id):
        self.logger.debug(f"Getting user todos from user_id {user_id}")
        self.logger.debug("Sending GET request..")
        return self.get(user_id=user_id)

    @step("Create user todo")
    def create_todo(self, user_id, data: dict = POST_DATA):
        self.logger.debug(f"Creating a todo for user with user_id {user_id}")
        self.logger.debug("Sending POST request..")
        return self.post(user_id=user_id, data=data)
