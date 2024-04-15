from methods.login_methods import LoginMethods
from methods.other_methods import OtherMethods
from methods.register_methods import RegisterMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import AUTH_REGISTER_ENDPOINT, AUTH_LOGIN_ENDPOINT
from utils.response_codes import ResponseCodes
from utils.response_assertion import ResponseJson
from utils.test_data import TestData


class TestRestApiLoginUser:

    @allure_step_decorator("Тест успешной авторизации пользователя, по логину и паролю")
    def test_login_user(self):
        email, password, name = OtherMethods.generation_data()
        RegisterMethods.create_user(AUTH_REGISTER_ENDPOINT, TestData.NONE_TOKEN, email, password, name)
        response = LoginMethods.login_user(AUTH_LOGIN_ENDPOINT, TestData.NONE_TOKEN, email, password)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_USER)

    @allure_step_decorator("Тест авторизации пользователя, с некорректными логином и паролем")
    def test_login_user_wrong_data(self):
        response = LoginMethods.login_user(AUTH_LOGIN_ENDPOINT, TestData.NONE_TOKEN, TestData.WRONG_EMAIL, TestData.WRONG_PASSWORD)

        assert response.status_code == ResponseCodes.UNAUTHORIZED.value
        assert response.json() == ResponseJson.LOGIN_USER_WRONG
