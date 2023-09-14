from dataclasses import dataclass, asdict

class UserDataModel:
    request_post_user_keys = ("name", "gender", "email", "status")
    response_post_user_keys = ("id", "name", "gender", "email", "status")
    response_put_user_keys = ("id", "name", "email", "status", "gender")


# @dataclass(frozen=True)
# class PostUserModel:
#     name: str
#     gender: str
#     email: str
#     status: str
#
# @dataclass(frozen=True)
# class PutUserModel:
#     name: str = None
#     email: str = None
#     status: str = None


