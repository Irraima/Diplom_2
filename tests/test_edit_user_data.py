import allure
import config
from conftest import register_and_delete_user
from stellar_burgers_api import StellarBurgersApi


class TestEditUserInfo:

    @allure.title('Проверка возможности поменять email авторизованного пользователя')
    def test_is_possible_to_edit_user_email(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        user_email = StellarBurgersApi.get_user_info(access_token).json()['user']['email']
        edit_user_email = StellarBurgersApi.edit_user_info(body={
            'email': f'test_{user_email}'
        },
            token=access_token)
        edited_user_email = StellarBurgersApi.get_user_info(access_token).json()['user']['email']
        assert edit_user_email.status_code == 200
        assert edited_user_email == f'test_{user_email}'

    @allure.title('Проверка возможности поменять username авторизованного пользователя')
    def test_is_possible_to_edit_user_name(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        user_name = StellarBurgersApi.get_user_info(access_token).json()['user']['name']
        edit_user_name = StellarBurgersApi.edit_user_info(body={
            'name': f'test_{user_name}'
        },
            token=access_token)
        edited_user_name = StellarBurgersApi.get_user_info(access_token).json()['user']['name']
        assert edit_user_name.status_code == 200
        assert edited_user_name == f'test_{user_name}'

    @allure.title('Проверка отсутствия возможности поменять email, если пользователь не авторизован')
    def test_impossible_to_edit_user_email_not_authorized(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        user_email = StellarBurgersApi.get_user_info(access_token).json()['user']['email']
        edit_user_email = StellarBurgersApi.edit_user_info(body={
            'email': f'test_{user_email}'
        },
            token='')
        edited_user_email = StellarBurgersApi.get_user_info(access_token).json()['user']['email']
        assert edit_user_email.status_code == 401
        assert edited_user_email == user_email
        assert edit_user_email.json()['message'] == config.ResponseMessages.SHOULD_BE_AUTHORIZED_TO_EDIT_USER_INFO_ERROR_TEXT

    @allure.title('Проверка отсутствия возможности поменять username, если пользователь не авторизован')
    def test_impossible_to_edit_user_name_not_authorized(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        user_name = StellarBurgersApi.get_user_info(access_token).json()['user']['name']
        edit_user_name = StellarBurgersApi.edit_user_info(body={
            'name': f'test_{user_name}'
        },
            token='')
        edited_user_name = StellarBurgersApi.get_user_info(access_token).json()['user']['name']
        assert edit_user_name.status_code == 401
        assert edited_user_name == user_name
        assert edit_user_name.json()['message'] == config.ResponseMessages.SHOULD_BE_AUTHORIZED_TO_EDIT_USER_INFO_ERROR_TEXT
