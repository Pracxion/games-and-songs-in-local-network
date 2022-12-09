from flask import request, session
from src.controller.base_api import BaseApi
from src.controller.main.utils.main import check_registration
from src.model.db_model.db import db
from src.model.db_model.user_model import User
from src.enum.status_codes import StatusCode


class RegisterApi(BaseApi):
    def post(self):
        try:
            new_user = check_registration(request.get_json())
            new_user = User(**new_user)
            new_user.hash_password()
            db.session.add(new_user)
            db.session.commit()
            id = new_user.id

            session["id"] = new_user.id

            return {"id": str(id)}, StatusCode.OK.value

        except Exception as e:
            return {"message": e}, StatusCode.BAD_REQUEST.value
        # TODO error handling
