import pytest
from api_client.users_api_client import UserApiClient
from api_client.posts_api_client import PostsApiClient
from api_client.comments_api_client import CommentsApiClient
from api_client.todos_api_client import TodosApiClient
from access.api_token import API_TOKEN

@pytest.fixture
def users_client():
    client = UserApiClient(api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def posts_client():
    client = PostsApiClient(api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def comments_client():
    client = CommentsApiClient(api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def todos_client():
    client = TodosApiClient(api_token=API_TOKEN)
    yield client
    del client
