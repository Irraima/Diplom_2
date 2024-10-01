import allure
import config
from conftest import register_and_delete_user
from stellar_burgers_api import StellarBurgersApi


class TestGetUserOrders:

    @allure.title('Проверка того, что авторизованный пользователь может получить заказы конкретного пользователя')
    def test_get_user_orders_authorized_user(self, register_and_delete_user):
        register = register_and_delete_user
        access_token = register.json()['accessToken']
        get_user_orders_response = StellarBurgersApi.get_user_orders(access_token)
        assert get_user_orders_response.status_code == 200
        assert get_user_orders_response.json()['success']
        assert get_user_orders_response.json()['orders'] == []

    @allure.title('Проверка того, что неавторизованный пользователь не может получить заказы конкретного пользователя')
    def test_get_user_orders_unauthorized_user(self, register_and_delete_user):
        get_user_orders_response = StellarBurgersApi.get_user_orders('')
        assert get_user_orders_response.status_code == 401
        assert not get_user_orders_response.json()['success']
        assert get_user_orders_response.json()['message'] == config.ResponseMessages.AUTH_REQUIRED_TO_GET_USER_ORDERS_ERROR_TEXT
