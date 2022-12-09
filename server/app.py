from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from src.db.db import initialize_db
from src.routes.routes import initialize_routes
from configuration import DevelopmentConfiguration


def create_app(config=DevelopmentConfiguration):
    # Core
    app: Flask = Flask(__name__)

    # Config
    app.config.from_object(config)

    # TODO add error handling
    api: Api = Api(app)
    bcrypt: Bcrypt = Bcrypt(app)
    jwt: JWTManager = JWTManager(app)

    with app.app_context():
        initialize_db(app)
        initialize_routes(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
