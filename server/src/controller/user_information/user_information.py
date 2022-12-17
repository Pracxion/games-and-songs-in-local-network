from flask import jsonify, session
from src.enum.status_codes import StatusCode
from src.controller.base_api import BaseApi
from src.exceptions.authorization import UnauthorizedError


class UserInformationApi(BaseApi):
    def get(self):
        try:
            if 'id' not in session:
                raise UnauthorizedError

        except Exception as exception:
            return {"error": str(type(exception).__name__)}, StatusCode.UNAUTHORIZED.value

        return jsonify({}), StatusCode.OK
