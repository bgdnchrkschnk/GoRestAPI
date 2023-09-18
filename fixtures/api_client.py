import pytest
from api_client.users_api_client import UserApiClient
from api_client.posts_api_client import PostsApiClient
from api_client.comments_api_client import CommentsApiClient
from api_client.todos_api_client import TodosApiClient
from access.api_token import API_TOKEN
from allure import title


@pytest.fixture
def users_client(custom_logger):
    client = UserApiClient(logger=custom_logger, api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def posts_client(custom_logger):
    client = PostsApiClient(logger=custom_logger, api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def comments_client(custom_logger):
    client = CommentsApiClient(logger=custom_logger, api_token=API_TOKEN)
    yield client
    del client

@pytest.fixture
def todos_client(custom_logger):
    client = TodosApiClient(logger=custom_logger, api_token=API_TOKEN)
    yield client
    del client
