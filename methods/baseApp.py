import logging
import requests

from utils.allure_decorator import allure_step_decorator


class BaseApp:


    @allure_step_decorator("Производим отправка POST запроса")
    def send_post_request(self, url, headers, data):
        try:
            response = requests.post(url, headers=headers, json=data)
            logging.info(f"Отправлен запрос POST по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса POST по {url}: {e}")
            return None

    @allure_step_decorator("Производим отправка GET запроса")
    def send_get_request(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            logging.info(f"Отправлен запрос GET по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса GET по {url}: {e}")
            return None

    @allure_step_decorator("Производим отправка PATCH запроса")
    def send_patch_request(self, url, headers, data):
        try:
            response = requests.patch(url, headers=headers, data=data)
            logging.info(f"Отправлен запрос PATCH по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса PATCH по {url}: {e}")
            return None
