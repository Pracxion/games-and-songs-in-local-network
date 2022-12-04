from ....exceptions.username import *
from ....exceptions.forename import *
from ....exceptions.surename import *
from ....exceptions.password import *
from ....db_models.user_model import User


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
