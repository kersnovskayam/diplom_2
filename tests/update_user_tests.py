from methods.other_methods import OtherMethods
from methods.update_user_methods import UpdateUserMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import AUTH_USER_ENDPOINT
from utils.response_codes import ResponseCodes
from utils.response_assertion import ResponseJson
from utils.test_data import TestData


class TestRestApiUpdateUser:

    other_methods = OtherMethods()

    @allure_step_decorator("Тест смены данных по почте пользователю")
    def test_update_email_user(self):
        token = self.other_methods.create_user_and_take_token()
        email, _, _, = self.other_methods.generation_data()
        response = UpdateUserMethods.update_user(AUTH_USER_ENDPOINT, token, email, TestData.NONE_VALUE)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_UPDATE_USER)

    @allure_step_decorator("Тест смены данных по почте и имени пользователю")
    def test_update_email_and_name_user(self):
        token = self.other_methods.create_user_and_take_token()
        email, _, _, = self.other_methods.generation_data()
        response = UpdateUserMethods.update_user(AUTH_USER_ENDPOINT, token, email, TestData.CREATED_NAME)

        assert response.status_code == ResponseCodes.SUCCESS.value
        assert all(key in response.json() for key in ResponseJson.SUCCESS_UPDATE_USER)

    @allure_step_decorator("Тест смены данных не авторизованного пользователя")
    def test_update_authorised_user(self):
        email, _, _, = self.other_methods.generation_data()
        response = UpdateUserMethods.update_user(AUTH_USER_ENDPOINT, TestData.NONE_VALUE, email, TestData.CREATED_NAME)

        assert response.status_code == ResponseCodes.UNAUTHORIZED.value
        assert response.json() == ResponseJson.UNAUTHORIZED_DATA
