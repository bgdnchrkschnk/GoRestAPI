from randomuser import RandomUser
import random

class UserPostDataProvider:

    @staticmethod
    def get_user_post_datamodel():
        name = RandomUser().get_first_name()
        gender = RandomUser().get_gender()
        email = RandomUser().get_email()
        status = "active"
        return dict(name=name, gender=gender, email=email, status=status)