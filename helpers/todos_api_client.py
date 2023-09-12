from api_client.base_api_client import BaseApiClient


class TodosEndpoint:

    @staticmethod
    def build_getdel_post_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        from api_client.todos_api_client import TodosApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id) + TodosApiClient.ENDPOINT
        return endpoint
