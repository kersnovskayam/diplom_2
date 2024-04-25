from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator


class LoginMethods(BaseApp):

    @allure_step_decorator("Метод по авторизации пользователя")
    def login_user(self, api_connection, token, email, password):
        headers = {'Authorization': token}
        data = {
            "email": email,
            "password": password,
        }

        response = self.send_post_request(api_connection, headers=headers, data=data)

        return response
