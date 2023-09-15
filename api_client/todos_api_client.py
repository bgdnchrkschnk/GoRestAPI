from api_client.base_api_client import BaseApiClient


class TodosApiClient(BaseApiClient):
    ENDPOINT = "/todos/"

    def get(self, user_id):
        from helpers.todos_api_client import TodosEndpoint
        endpoint = TodosEndpoint.build_getpost_todos_endpoint(user_id=user_id)
        return self._get(endpoint=endpoint)

    def post(self, user_id):
        from helpers.todos_api_client import TodosEndpoint
        endpoint = TodosEndpoint.build_getpost_todos_endpoint(user_id=user_id)
        return self._post(endpoint=endpoint, data=data)

    def retrieve_todos(self):
        from helpers.todos_api_client import TodosEndpoint
        return self._retrieve(endpoint=TodosEndpoint.build_retrieve_todos_endpoint())

    def find_todo(self, user_id):
        return self.get(user_id=user_id)

    def create_todo(self, user_id):
        return self.post(user_id=user_id)
