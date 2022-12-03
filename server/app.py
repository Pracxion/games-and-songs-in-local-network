from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from db_models.db import initialize_db
from routes.routes import initialize_routes
from configuration import DevelopmentConfiguration


def create_app(config=DevelopmentConfiguration):
    # Core
    app = Flask(__name__)

    # Config
    app.config.from_object(config)

    # TODO add error handling
    api = Api(app)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    with app.app_context():
        initialize_db(app)
        initialize_routes(api)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
