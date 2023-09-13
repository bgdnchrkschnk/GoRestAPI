from randomuser import RandomUser
import random


class PostCommentDataProvider:

    @staticmethod
    def get_post_comment_datamodel():
        name = RandomUser().get_first_name()
        gender = RandomUser().get_gender()
        email = RandomUser().get_email()
        status = "active"
        return dict(name=name, gender=gender, email=email, status=status)
