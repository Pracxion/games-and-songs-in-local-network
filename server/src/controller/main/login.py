from flask import request
from src.controller.base_api import BaseApi
from src.exceptions.not_a_object import NotAJsonObjectException
from src.controller.main.utils.main import validate_login_credentials
from src.enum.status_codes import StatusCode
import datetime
from flask_jwt_extended import create_access_token


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
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=user_information["id"], expires_delta=expires)
            return {"id": user_information["id"], "token": access_token}, StatusCode.OK.value
