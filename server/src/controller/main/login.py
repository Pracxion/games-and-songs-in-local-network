from flask import redirect, request, session
from src.controller.base_api import BaseApi
from src.exceptions.not_a_object import NotAJsonObjectException
from src.controller.main.utils.main import validate_login_credentials
from src.enum.status_codes import StatusCode


class LoginApi(BaseApi):
    def post(self):
        try:
            if request.is_json:
                user_information = validate_login_credentials(request.get_json())
            else:
                raise NotAJsonObjectException

        except Exception as exception:
            return {"error": str(type(exception).__name__)}, StatusCode.BAD_REQUEST.value

        else:
            session["id"] = user_information["id"]
            return {}, StatusCode.OK.value
