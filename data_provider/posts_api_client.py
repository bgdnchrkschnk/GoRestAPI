from randomuser import RandomUser


class UserPostDataProvider:

    @staticmethod
    def get_user_post_datamodel():
        title = RandomUser().get_full_name(capitalize=True)
        body = RandomUser().get_state(capitalize=True)
        return dict(title=title, body=body)