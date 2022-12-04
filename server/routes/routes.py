from .main.login import LoginApi
from .main.register import RegisterApi

from .user_information.user_information import UserInformationApi


def initialize_routes(api):
    api.add_resource(LoginApi, "/login")
    api.add_resource(RegisterApi, "/register")

    api.add_resource(UserInformationApi, "/@me")
