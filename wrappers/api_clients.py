from exceptions.base_api_client import ApiTokenNotFoundError
from allure import attach, attachment_type

def api_token_wrapper(func):
    def wrapper(self, *args, **kwargs):
        if self.api_token:
            return func(self, *args, **kwargs)
        else:
            raise ApiTokenNotFoundError("No API token found for the request!")
    return wrapper

def attach_allure_data_wrapper(func):
    def wrapper(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        attach(str(res.json()), attachment_type=attachment_type.TEXT, name=f"{func.__name__} - response json")
        return res
    return wrapper
