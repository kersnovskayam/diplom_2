from methods.orders_methods import OrderMethods
from methods.other_methods import OtherMethods

from utils.allure_decorator import allure_step_decorator
from utils.constants import ORDERS_CREATE_ENDPOINT
from utils.response_codes import ResponseCodes
from utils.response_assertion import ResponseJson
from utils.test_data import TestData


class TestRestApiGetOrders:

    @allure_step_decorator("Тест получения списка заказов конкретного пользователя")
    def test_get_orders(self):
        token = OtherMethods.create_user_and_take_token()
        OrderMethods.create_order(ORDERS_CREATE_ENDPOINT, token, TestData.CORRECT_INGRIDIENTS)
        response = OrderMethods.get_orders(ORDERS_CREATE_ENDPOINT, token)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_GET_ORDER)

    @allure_step_decorator("Тест получения списка заказов неавторизованного  пользователя")
    def test_get_orders_authorised_user(self):
        response = OrderMethods.get_orders(ORDERS_CREATE_ENDPOINT, TestData.NONE_TOKEN)

        assert response.status_code == ResponseCodes.UNAUTHORIZED.value
        assert all(key in response.json() for key in ResponseJson.UNAUTHORIZED_DATA)
