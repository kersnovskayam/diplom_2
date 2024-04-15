from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator


class RegisterMethods:

    @staticmethod
    @allure_step_decorator("Метод по созданию пользователя")
    def create_user(api_connection, token, email, password, name):
        headers = {'Authorization': token}
        data = {
            "email": email,
            "password": password,
            "name": name
        }

        response = BaseApp.send_post_request(api_connection, headers, data)

        return response
