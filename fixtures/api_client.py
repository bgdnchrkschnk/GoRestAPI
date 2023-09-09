import pytest
from api_client.users_api_client import UserApiClient
from api_client.posts_api_client import PostsApiClient
from api_client.comments_api_client import CommentsApiClient
from api_client.todos_api_client import TodosApiClient
from access.api_token import API_TOKEN


@pytest.fixture
def users_client():
    client = UserApiClient(API_TOKEN)
    yield client
    del client

@pytest.fixture
def posts_client():
    client = PostsApiClient()
    yield client
    del client

@pytest.fixture
def comments_client():
    client = CommentsApiClient()
    yield client
    del client

@pytest.fixture
def todos_client():
    client = TodosApiClient()
    yield client
    del client
