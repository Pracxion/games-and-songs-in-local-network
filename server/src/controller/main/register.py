from flask import request
from src.controller.base_api import BaseApi
from src.controller.main.utils.main import check_registration
from src.model.db_model.user_model import User


class RegisterApi(BaseApi):
    def post(self):
        print("hallo")
        try:
            new_user = check_registration(request)
            print(new_user)
            user = User(new_user)
            user.hash_password()
            user.save()
            id = user.id
            return {"id": str(id)}, 200
        except:
            return {"id": "id"}
        # TODO error handling
