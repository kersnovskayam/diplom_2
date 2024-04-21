from methods.other_methods import OtherMethods
from methods.register_methods import RegisterMethods
from utils.allure_decorator import allure_step_decorator
from constants import AUTH_REGISTER_ENDPOINT
from utils.response_codes import ResponseCodes
from utils.response_assertion import ResponseJson
from utils.test_data import TestData


class TestRestApiCreateUser:

    @allure_step_decorator("Тест создания уникального пользователя")
    def test_create_unique_user(self):
        email, password, name = OtherMethods.generation_data()
        response = RegisterMethods.create_user(AUTH_REGISTER_ENDPOINT, TestData.NONE_VALUE, email, password, name)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_USER)

    @allure_step_decorator("Тест создания существующего пользователя")
    def test_create_exists_user(self):
        response = RegisterMethods.create_user(AUTH_REGISTER_ENDPOINT, TestData.NONE_VALUE, TestData.CREATED_EMAIL, TestData.CREATED_PASSWORD, TestData.CREATED_NAME)

        assert response.status_code == ResponseCodes.FORBIDDEN.value
        assert response.json() == ResponseJson.CREATE_USER_EXISTS

    @allure_step_decorator("Тест создания пользователя без передачи данных по паролю и имени ")
    def test_create_user_without_required_fields(self):
        response = RegisterMethods.create_user(AUTH_REGISTER_ENDPOINT, TestData.NONE_VALUE, TestData.CREATED_EMAIL, TestData.NONE_VALUE, TestData.NONE_VALUE)

        assert response.status_code == ResponseCodes.FORBIDDEN.value
        assert response.json() == ResponseJson.CREATE_USER_WITHOUT_REQUIRED_FIELDS

