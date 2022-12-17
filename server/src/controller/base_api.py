from flask_restful import Resource
from src.enum.status_codes import StatusCode

class BaseApi(Resource):

    def post(self):
        return {}, StatusCode.METHOD_NOT_ALLOWED.value

    def get(self):
        return {}, StatusCode.METHOD_NOT_ALLOWED.value

    def put(self):
        return {}, StatusCode.METHOD_NOT_ALLOWED.value

    def delete(self):
        return {}, StatusCode.METHOD_NOT_ALLOWED.value
