from ..base_api import BaseApi
from flask import jsonify

class MainApi(BaseApi):
    def get(self):
        return jsonify({})
