from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator


class UpdateUserMethods:

    @staticmethod
    @allure_step_decorator("Метод по обновлению данных пользователя")
    def update_user(api_connection, token, email, name):
        headers = {'Authorization': token}
        data = {
            "email": email,
            "name": name
        }

        response = BaseApp.send_patch_request(api_connection, headers=headers, data=data)

        return response
