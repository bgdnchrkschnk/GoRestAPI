from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class PostUserModel:
    name: str
    gender: str
    email: str
    status: str

post_user_keys = ("name", "gender", "email", "status")

@dataclass(frozen=True)
class PutUserModel:
    name: str = None
    email: str = None
    status: str = None

put_user_keys = ("name", "email", "status")
