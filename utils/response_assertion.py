class ResponseJson:
    CREATE_USER_EXISTS = {'success': False, 'message': 'User already exists'}
    CREATE_USER_WITHOUT_REQUIRED_FIELDS = {'message':'Email, password and name are required fields', 'success': False}
    LOGIN_USER_WRONG = {'success': False, 'message': 'email or password are incorrect'}
    SUCCESS_USER = ['success', 'user', 'accessToken', 'refreshToken']
    UNAUTHORIZED_DATA = {'success': False, 'message': 'You should be authorised'}
    SUCCESS_UPDATE_USER = ['success', 'user']
    SUCCESS_CREATE_ORDER = ['success', 'name', 'order']
    ORDER_WRONG_INGRIDIENTS = {'success': False, 'message': 'One or more ids provided are incorrect'}
    EMPTY_INGRIDIENTS = {'success': False, 'message': 'Ingredient ids must be provided'}
    SUCCESS_GET_ORDER = ['success', 'orders']

