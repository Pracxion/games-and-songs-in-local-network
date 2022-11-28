from flask import Flask
from flask import request, jsonify, session
from flask_session import Session
from flask_bcrypt import Bcrypt
from db_models.user_model import db, User
from exceptions.registration import *
from configuration import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = Configuration.APP_SECRET_KEY

bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def index():
    return {}


def check_registration(request) -> tuple[str, str, str, str]:

    # Username check
    if "username" not in request:
        raise UsernameNotInRequestException

    if not 3 <= len(request["username"]) <= 20:
        raise UsernameLengthException

    username_set = set(str(request["username"]))
    username_allowed_symbols = set(Configuration.USERNAME_ALLOWED_SYMBOLS)
    if len(username_set - username_allowed_symbols) > 0:
        raise UsernameDisallowedSymbolsException

    username_exists = User.query.filter_by(username=request["username"]).first() is not None

    # Forename check
    if "forename" not in request:
        raise ForenameNotInRequestException

    if not 3 <= len(request["forename"]) <= 20:
        raise ForenameLengthException

    forename_set = set(str(request["username"]))
    forename_allowed_symbols = set(Configuration.NAME_ALLOWED_SYMBOLS)
    if len(forename_set - forename_allowed_symbols) > 0:
        raise ForenameDisallowedSymbolsException

    # Surename check
    if "surename" not in request:
        raise SurenameNotInRequestException

    if not 3 <= len(request["surename"]) <= 20:
        raise SurenameLengthException

    surename_set = set(str(request["username"]))
    surename_allowed_symbols = set(Configuration.NAME_ALLOWED_SYMBOLS)
    if len(surename_set - surename_allowed_symbols) > 0:
        raise SurenameDisallowedSymbolsException

    # Password
    if "password" not in request:
        raise PasswordNotInRequestException

    if not 6 <= len(request["password"]):
        raise PasswordLengthException

    password_set = set(str(request["password"]))
    password_allowed_symbols = set(Configuration.PASSWORD_ALLOWED_SYMBOLS)
    if len(password_set - password_allowed_symbols) > 0:
        raise PasswordDisallowedSymbolsException

    return (str(request["username"]), str(request["forename"]), str(request["surename"]), str(request["password"]))


@app.route("/register", methods=["POST"])
def register_user():
    try:
        username, forename, surename, password = check_registration(request)
    except:
        # TODO Exception Handling for wrong inputs in registration fields
        pass
    else:
        hashed_password = bcrypt.generate_password_hash(password)
        new_user = User(username=username, forename=forename.lower(), surename=surename.lower(), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"id": new_user.id, "username": new_user.username, "forename": new_user.forename, "surename": new_user.surename})


@app.route("/login", methods=["POST"])
def login_user():
    pass


@app.route("/logout")
def logout_user():
    pass


if __name__ == "__main__":
    app.run(debug=True)
