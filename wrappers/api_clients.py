from exceptions.base_api_client import ApiTokenNotFoundError

def api_token_wrapper(func):
    def wrapper(self, *args, **kwargs):
        if self.api_token:
            return func(self, *args, **kwargs)
        else:
            raise ApiTokenNotFoundError("No API token found for the request!")
    return wrapper