from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class PostUserModel:
    name: str
    gender: str
    email: str
    status: str


@dataclass(frozen=True)
class PutUserModel:
    name: str = None
    email: str = None
    status: str = None
