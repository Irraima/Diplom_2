import pytest
import requests
from stellar_burgers_api import StellarBurgersApi
import config
import data


@pytest.fixture
def delete_user():
    def _delete_user(token):
        StellarBurgersApi.delete_user(token)
    yield _delete_user


@pytest.fixture
def register_and_delete_user():
    register_user_response = StellarBurgersApi.create_user(data.UserData.create_user_data)
    access_token = register_user_response.json()['accessToken']

    yield register_user_response

    requests.delete(f'{config.Urls.SB_URL}{config.Urls.DELETE_USER_PATH}', headers={
        'Authorization': access_token
    })
