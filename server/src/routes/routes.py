from flask_restful import Api

from src.api.main.login import LoginApi
from src.api.main.register import RegisterApi

from src.api.user_information.user_information import UserInformationApi


def initialize_routes(api: Api) -> None:
    api.add_resource(LoginApi, "/login")
    api.add_resource(RegisterApi, "/register")

    api.add_resource(UserInformationApi, "/@me")
