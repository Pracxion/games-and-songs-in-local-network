from flask import Flask
from flask_cors import CORS
from flask_session import Session
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from src.model.db_model.db import initialize_db
from src.routes.routes import initialize_routes
from configuration import DevelopmentConfiguration


def create_app(config=DevelopmentConfiguration):
    # Core
    app: Flask = Flask(__name__)

    # Config
    app.config.from_object(config)
    app.secret_key = config.SECRET_KEY
    # TODO add error handling
    api: Api = Api(app)
    CORS(app, supports_credentials=True)
    Session(app)
    Bcrypt(app)
    JWTManager(app)

    with app.app_context():
        initialize_db(app)
        initialize_routes(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
