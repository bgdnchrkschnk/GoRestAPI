from randomuser import RandomUser
import random

from data_models.users_api_client import UserDataModel
from exceptions.users_api_client import InvalidUserDataModelDict


class PostUserDataProvider:

    @staticmethod
    def get_post_user_datamodel():
        name = RandomUser().get_first_name()
        gender = RandomUser().get_gender()
        email = RandomUser().get_email()
        status = "active"
        yield dict(name=name, gender=gender, email=email, status=status)


class PutUserDataProvider:

    @staticmethod
    def get_put_user_datamodel():
        dict_user = dict()
        choice = (True, False)
        while not dict_user:
            name = RandomUser().get_first_name()
            email = RandomUser().get_email()
            status = random.choice(["active", "inactive"])
            if random.choice(choice):
                dict_user["name"] = name
            if random.choice(choice):
                dict_user["email"] = email
            if random.choice(choice):
                dict_user["status"] = status
        yield dict_user