from enum import Enum


class StatusCode(Enum):
    # 2XX
    OK: int = 200
    CREATED: int = 201
    ACCEPTED: int = 202
    NO_CONTENT: int = 204
    RESET_CONTENT: int = 205
    # 4XX
    BAD_REQUEST: int = 400
    UNAUTHORIZED: int = 401
    PAYMENT_REQUIRED: int = 402
    FORBIDDEN: int = 403
    NOT_FOUND: int = 404
    METHOD_NOT_ALLOWED: int = 405
    REQUEST_TIMEOUT: int = 408
    # 5XX
    INTERNAL_SERVER_ERROR: int = 500
    NOT_IMPLEMENTED: int = 501
    BAD_GATEWAY: int = 502
    SERVICE_UNAVAILABLE: int = 503
    GATEWAY_TIMEOUT: int = 504
