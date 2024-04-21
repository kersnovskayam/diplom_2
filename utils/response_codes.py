from enum import Enum

class ResponseCodes(Enum):
    SUCCESS = 200
    FORBIDDEN = 403
    BAD_REQUEST = 400
    UNAUTHORIZED = 401

