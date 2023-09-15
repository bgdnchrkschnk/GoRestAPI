from api_client.base_api_client import BaseApiClient
from api_client.users_api_client import UserApiClient
from api_client.todos_api_client import TodosApiClient


class TodosEndpoint:

    @staticmethod
    def build_getpost_todos_endpoint(user_id):
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id) + TodosApiClient.ENDPOINT
        return endpoint

    @staticmethod
    def build_retrieve_todos_endpoint():
        from api_client.todos_api_client import TodosApiClient
        endpoint = BaseApiClient.BASE_URL + TodosApiClient.ENDPOINT
        return endpoint