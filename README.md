## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки ручек, позволяющих создть, авторизовать или изменить пользователя в Stellar Burgers, 
а так же создать заказ или получить данные о заказе конкретного пользователя

### Реализованные сценарии

Созданы API-тесты - `test_registration`, `test_auth_user`, `test_edit_user_data`, `test_create_order`, `test_get_user_orders`

### Структура проекта

- `tests` - пакет, содержащий тесты ручек
- `stellar_burgers_api` - файл, содержащий ручки

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`
 
**Создание allure отчета** 

> `$ pytest tests --alluredir=allure_results`
 
**Открыть allure отчет в формате веб страницы**

> `$ allure serve allure_results`