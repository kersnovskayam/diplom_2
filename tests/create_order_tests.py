from methods.orders_methods import OrderMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import AUTH_REGISTER_ENDPOINT, ORDERS_CREATE_ENDPOINT
from utils.response_codes import ResponseCodes
from utils.response_assertion import ResponseJson
from utils.test_data import TestData


class TestRestApiCreateOrders:
    other_methods = OtherMethods()
    order_methods = OrderMethods()

    @allure_step_decorator("Тест создания заказа под авторизованным пользователем")
    def test_create_order(self):
        token = self.other_methods.create_user_and_take_token()
        response = self.order_methods.create_order(ORDERS_CREATE_ENDPOINT, token, TestData.CORRECT_INGRIDIENTS)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_CREATE_ORDER)

    @allure_step_decorator("Тест создания заказа под авторизованным пользователем с передачей неверного хеша ингридиентов")
    def test_create_order_wrong_ingridients(self):
        token = self.other_methods.create_user_and_take_token()
        response = self.order_methods.create_order(ORDERS_CREATE_ENDPOINT, token, TestData.WRONG_HASH_INGRIDIENTS)

        assert response.status_code == ResponseCodes.BAD_REQUEST.value
        assert all(key in response.json() for key in ResponseJson.ORDER_WRONG_INGRIDIENTS)

    @allure_step_decorator("Тест создания заказа под авторизованным пользователем с без передачи хеша ингридиентов")
    def test_create_order_without_ingridients(self):
        token = self.other_methods.create_user_and_take_token()
        response = self.order_methods.create_order(ORDERS_CREATE_ENDPOINT, token, TestData.NONE_VALUE)

        assert response.status_code == ResponseCodes.BAD_REQUEST.value
        assert all(key in response.json() for key in ResponseJson.EMPTY_INGRIDIENTS)

    @allure_step_decorator("Тест создания заказа под авторизованным пользователем с без передачи хеша ингридиентов")
    def test_create_order_authorised_user(self):
        response = self.order_methods.create_order(AUTH_REGISTER_ENDPOINT, TestData.NONE_VALUE, TestData.NONE_VALUE)

        assert response.status_code == ResponseCodes.FORBIDDEN.value
        assert all(key in response.json() for key in ResponseJson.EMPTY_INGRIDIENTS)
