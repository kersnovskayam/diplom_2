import random
import string

from methods.register_methods import RegisterMethods
from constants import AUTH_REGISTER_ENDPOINT
from utils.test_data import TestData


class OtherMethods:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generation_data():
        email = OtherMethods.generate_random_string(10)
        password = OtherMethods.generate_random_string(10)
        name = OtherMethods.generate_random_string(10)
        email_address = f"{email}@yandex.ru"

        return email_address, password, name

    @staticmethod
    def create_user_and_take_token():
        email, password, name = OtherMethods.generation_data()
        response = RegisterMethods.create_user(AUTH_REGISTER_ENDPOINT, TestData.NONE_TOKEN, email, password, name)
        token = response.json()['accessToken']

        return token
