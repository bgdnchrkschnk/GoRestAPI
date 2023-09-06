from api_client.base_api_client import BaseApiClient
from api_client.users_api_client import UserApiClient


class UsersEndpoints:

    @staticmethod
    def build_get_users_endpoint(user_id):
        endpoint = BaseApiClient.BASE_URL + UserApiClient.ENDPOINT + str(user_id)
        return endpoint

    @staticmethod
    def build_post_users_endpoint():
        pass
