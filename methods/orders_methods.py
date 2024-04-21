from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator


class OrderMethods:

    @staticmethod
    @allure_step_decorator("Метод по созданию заказа")
    def create_order(api_connection, token, ingredients):
        headers = {'Authorization': token,
                   'Content-type': 'application/json'
                   }
        data = {
            'ingredients': ingredients
        }

        response = BaseApp.send_post_request(api_connection, headers=headers, data=data)

        return response

    @staticmethod
    @allure_step_decorator("Метод по получению данных о заказах пользователя")
    def get_orders(api_connection, token):
        headers = {'Authorization': token,
                   'Content-type': 'application/json'
                   }

        response = BaseApp.send_get_request(api_connection, headers=headers)

        return response

