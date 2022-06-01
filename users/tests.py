from django.test import TestCase
import pytest
from factories import *
# Create your tests here.

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def random_user():
    return UsersFactory()

@pytest.mark.django_db
@pytest.mark.parametrize(
    "tested_uri,response_status",
    [
        ('/users/', status.HTTP_403_FORBIDDEN),
        ('/person/', status.HTTP_403_FORBIDDEN)
    ]
)
def test_get_data_as_anonymouse_user(api_client):
    pass