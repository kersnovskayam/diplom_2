BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

ORDER_ENDPOINT = "orders/"
AUTH_ENDPOINT = "auth/"

# ========================================================= #
# GET - данные по заказам пользователя
# POST - Создание заказа.
ORDERS_CREATE_ENDPOINT = f"{BASE_URL}{ORDER_ENDPOINT}"

# ========================================================= #

# POST - Создание пользователя.
AUTH_REGISTER_ENDPOINT = f"{BASE_URL}{AUTH_ENDPOINT}register/"

# POST - Эндпоинт для авторизации.
AUTH_LOGIN_ENDPOINT = f"{BASE_URL}{AUTH_ENDPOINT}login/"

# GET - эндпоинт получения данных о пользователе.
AUTH_USER_ENDPOINT = f"{BASE_URL}{AUTH_ENDPOINT}user/"

# ========================================================= #
