import allure
import config
from conftest import register_and_delete_user
import data
from stellar_burgers_api import StellarBurgersApi


class TestRegistration:

    @allure.title('Проверка создания пользователя с валидными данными')
    def test_registration_with_valid_data(self, register_and_delete_user):
        register_user_response = register_and_delete_user
        assert register_user_response.status_code == 200
        assert register_user_response.json()['accessToken'] != ''

    @allure.title('Проверка возможности создания пользователя, который уже есть в базе данных')
    def test_register_already_existing_user(self):
        response = StellarBurgersApi.create_user(data.UserData.registered_user_data)
        assert response.status_code == 403
        assert response.json()['message'] == config.ResponseMessages.USER_ALREADY_EXISTS_ERROR_TEXT
        assert not response.json()['success']

    @allure.title('Проверка появления ошибки при создании пользователя, если не заполнено обязательное поле password')
    def test_registration_password_field_is_not_filled(self):
        register_user_response = StellarBurgersApi.create_user(data.UserData.create_user_data_empty_required_field)
        assert register_user_response.status_code == 403
        assert register_user_response.json()['message'] == config.ResponseMessages.MISSING_REQUIRED_FILED_ERROR_TEXT
        assert not register_user_response.json()['success']
