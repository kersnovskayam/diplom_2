import allure

def allure_step_decorator(step_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with allure.step(step_name + f" with arguments: {args}, {kwargs}"):
                return func(*args, **kwargs)
        return wrapper
    return decorator
