from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.enum.status_codes import StatusCode
from src.controller.base_api import BaseApi
from src.exceptions.authorization import UnauthorizedError


class UserInformationApi(BaseApi):
    @jwt_required
    def get(self):
        try:
            user = get_jwt_identity()
            if user is None:
                raise UnauthorizedError

        except Exception as exception:
            return {"error": str(type(exception).__name__)}, StatusCode.UNAUTHORIZED.value

        return jsonify(logged_in_as=user), StatusCode.OK
