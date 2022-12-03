from .main.main import MainApi
from .main.login import LoginApi
from .main.register import RegisterApi


def initialize_routes(api):
    api.add_resource(MainApi, "/")
    api.add_resource(LoginApi, "/login")
    api.add_resource(RegisterApi, "/register")
