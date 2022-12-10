from flask import request, session
from src.controller.base_api import BaseApi
from src.controller.main.utils.main import check_registration
from src.model.db_model.db import db
from src.model.db_model.user_model import User
from src.enum.status_codes import StatusCode
from src.exceptions.not_a_object import NotAJsonObjectException
import datetime
from flask_jwt_extended import create_access_token


class RegisterApi(BaseApi):
    def post(self):
        try:
            if request.is_json:
                new_user = check_registration(request.get_json())
            else:
                raise NotAJsonObjectException

        except Exception as exception:
            return {"error": str(type(exception).__name__)}, StatusCode.BAD_REQUEST.value

        else:
            new_user = User(**new_user)
            new_user.hash_password()
            db.session.add(new_user)
            db.session.commit()
            id = str(new_user.id)
            session["id"] = id
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=id, expires_delta=expires)
            return {"id": id, "token": access_token}, StatusCode.OK.value
