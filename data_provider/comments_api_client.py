from randomuser import RandomUser


class PostCommentDataProvider:

    @staticmethod
    def get_post_comment_datamodel():
        name = RandomUser().get_first_name()
        email = RandomUser().get_email()
        body = RandomUser().get_state(capitalize=True)
        yield dict(name=name, email=email, body=body)