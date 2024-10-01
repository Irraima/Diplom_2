import allure
import config
from conftest import register_and_delete_user
import data
from stellar_burgers_api import StellarBurgersApi


class TestCreateOrder:

    @allure.title('Проверка возможности создать заказ, если пользователь авторизован и добавлены ингредиенты')
    def test_create_order_with_authorization(self, register_and_delete_user):
        register_response = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        create_order_response = StellarBurgersApi.create_order(access_token, data.OrderData.create_order_data)
        assert create_order_response.status_code == 200
        assert create_order_response.json()['success']
        assert create_order_response.json()['order']['ingredients'][0]['_id'] == data.OrderData.create_order_data['ingredients'][0]

    @allure.title('Проверка возможности создать заказ, если пользователь не авторизован')
    def test_create_order_not_authorized(self):
        access_token = ''
        create_order_response = StellarBurgersApi.create_order(access_token, data.OrderData.create_order_data)
        assert create_order_response.status_code == 200
        assert create_order_response.json()['success']
        assert create_order_response.json()['order']['number'] != ''

    @allure.title('Проверка отсутствия возможности создать заказ, не добавив ни одного ингредиента')
    def test_create_order_no_ingredients(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        create_order_response = StellarBurgersApi.create_order(access_token, data.OrderData.order_data_no_ingredients)
        assert create_order_response.status_code == 400
        assert not create_order_response.json()['success']
        assert create_order_response.json()['message'] == config.ResponseMessages.CREATE_ORDER_INGREDIENTS_REQUIRED_ERROR_TEXT


    @allure.title('Проверка отсутствия возможности создать заказ, если указан невалидный хэш ингреденитов')
    def test_create_order_invalid_ingredient_hash(self, register_and_delete_user):
        register_user = register_and_delete_user
        access_token = register_and_delete_user.json()['accessToken']
        create_order_response = StellarBurgersApi.create_order(access_token, data.OrderData.invalid_ingredient_hash_data)
        assert create_order_response.status_code == 500
