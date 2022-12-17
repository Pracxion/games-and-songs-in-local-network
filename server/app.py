from flask import Flask
from src.model.db_model.db import initialize_db
from src.model.db_model.db import db
from flask_cors import CORS
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_session import Session
from src.routes.routes import initialize_routes
from configuration import DevelopmentConfiguration


def create_app(config=DevelopmentConfiguration):
    # Core
    app: Flask = Flask(__name__)

    # Config
    app.config.from_object(config)

    api: Api = Api(app)
    CORS(app, resources={r"*": {"origins": "http://localhost:5000"}}, expose_headers=["Content-Type", "X-CSRFToken"], supports_credentials=True)
    Bcrypt(app)
    JWTManager(app)
    sess = Session(app)

    with app.app_context():
        initialize_db(app)
        initialize_routes(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
