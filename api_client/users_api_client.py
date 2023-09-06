from api_client.base_api_client import BaseApiClient
from helpers.users_api_client import UsersEndpoints


class UserApiClient(BaseApiClient):
    ENDPOINT = "/users/"

    def __init__(self, api_token=None):
        super().__init__(api_token=api_token)

    def get(self, user_id: int, **kwargs):
        endpoint = UsersEndpoints.build_get_users_endpoint(user_id=user_id)
        return self._get(endp=endpoint, **kwargs)
