import allure
import config
from stellar_burgers_api import StellarBurgersApi
import data


class TestAuthorization:

    @allure.title('Проверка, что зарегистрированный пользователь может успешно авторизоваться')
    def test_existing_user_can_successfully_login(self):
        response = StellarBurgersApi.auth(data.UserData.registered_user_data['email'],
                                          data.UserData.registered_user_data['password'])
        assert response.status_code == 200
        assert response.json()['success']
        assert data.UserData.registered_user_data['email'].lower() in response.json()['user']['email']

    @allure.title('Проверка появления ошибки при попытке авторизации с неверно заполенными полями')
    def test_auth_with_wrong_password_and_wrong_email(self):
        response = StellarBurgersApi.auth(f'-{data.UserData.registered_user_data['email']}',
                                          f'-{data.UserData.registered_user_data['password']}')
        assert response.status_code == 401
        assert not response.json()['success']
        assert response.json()['message'] == config.ResponseMessages.INCORRECT_EMAIL_OR_PASSWORD_ERROR_TEXT
