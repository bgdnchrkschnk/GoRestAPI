from api_client.base_api_client import BaseApiClient


class UsersEndpoints:

    @staticmethod
    def build_get_users_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id)
        return endpoint

    @staticmethod
    def build_post_users_endpoint():
        from api_client.users_api_client import UserApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT
        return endpoint

    @staticmethod
    def build_put_users_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id)
        return endpoint

    @staticmethod
    def build_delete_users_endpoint(user_id):
        from api_client.users_api_client import UserApiClient
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id)
        return endpoint
