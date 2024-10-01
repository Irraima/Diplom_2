import requests
import allure
import config


class StellarBurgersApi:

    @staticmethod
    @allure.step('Отправить запрос на регистрацию пользователя')
    def create_user(body):
        return requests.post(f'{config.Urls.SB_URL}{config.Urls.CREATE_USER_PATH}',
                             json=body)

    @staticmethod
    @allure.step('Отправить запрос на удаление пользователя')
    def delete_user(token):
        return requests.delete(f'{config.Urls.SB_URL}{config.Urls.DELETE_USER_PATH}', headers={
            'Authorization': token
        })

    @staticmethod
    @allure.step('Отправить запрос на авторизацию пользователя')
    def auth(email, password):
        return requests.post(f'{config.Urls.SB_URL}{config.Urls.AUTH_PATH}', json={
            "email": email,
            "password": password
        })

    @staticmethod
    @allure.step('Получить информацию о пользователе')
    def get_user_info(token):
        return (requests.get(f'{config.Urls.SB_URL}{config.Urls.GET_USER_INFO_PATH}', headers={
            'Authorization': token
        }))

    @staticmethod
    @allure.step('Изменить информацию о пользователе')
    def edit_user_info(body, token):
        return requests.patch(f'{config.Urls.SB_URL}{config.Urls.EDIT_USER_INFO_PATH}', headers={
            'Authorization': token
        },
                              json=body)

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(token, body):
        return requests.post(f'{config.Urls.SB_URL}{config.Urls.CREATE_ORDER_PATH}', headers={
            'Authorization': token
        },
                              json=body)

    @staticmethod
    @allure.step('Получить список ингредиентов')
    def get_ingredients(token):
        return requests.get(f'{config.Urls.SB_URL}{config.Urls.GET_INGREDIENTS_PATH}', headers={
            'Authorization': token
        })

    @staticmethod
    def get_all_orders(token):
        return requests.get(f'{config.Urls.SB_URL}{config.Urls.GET_ALL_ORDERS_PATH}', headers={
            'Authorization': token
        })

    @staticmethod
    def get_user_orders(token):
        return requests.get(f'{config.Urls.SB_URL}{config.Urls.GET_USER_ORDERS_PATH}', headers={
            'Authorization': token
        })
