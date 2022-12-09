from src.exceptions.forname import FornameDisallowedSymbolsException, FornameLengthException, FornameNotInRequestException
from src.exceptions.surname import SurnameDisallowedSymbolsException, SurnameLengthException, SurnameNotInRequestException
from src.exceptions.password import PasswordDisallowedSymbolsException, PasswordLengthException, PasswordNotInRequestException
from src.exceptions.username import (
    UsernameDisallowedSymbolsException,
    UsernameExistsAlreadyException,
    UsernameLengthException,
    UsernameNotInRequestException,
)
from src.db.user_model import User
from src.enum.allowed_symbols import AllowedSymbols


def is_username_accepted(username: str) -> None:

    if not 3 <= len(username) <= 20:
        raise UsernameLengthException

    username_set = set(username)
    username_allowed_symbols = set(AllowedSymbols.USERNAME_ALLOWED_SYMBOLS.value)
    if len(username_set - username_allowed_symbols) > 0:
        raise UsernameDisallowedSymbolsException

    username_exists = User.query.filter_by(username=username).first() is not None
    # TODO raise error


def is_forname_accepted(forname: str) -> None:

    if not 3 <= len(forname) <= 20:
        raise FornameLengthException

    forname_set = set(forname)
    forname_allowed_symbols = set(AllowedSymbols.NAME_ALLOWED_SYMBOLS.value)
    if len(forname_set - forname_allowed_symbols) > 0:
        raise FornameDisallowedSymbolsException


def is_surname_accepted(surname: str) -> None:

    if not 3 <= len(surname) <= 20:
        raise SurnameLengthException

    surname_set = set(surname)
    surname_allowed_symbols = set(AllowedSymbols.NAME_ALLOWED_SYMBOLS.value)
    if len(surname_set - surname_allowed_symbols) > 0:
        raise SurnameDisallowedSymbolsException


def is_password_accepted(password: str) -> None:

    if not 6 <= len(password):
        raise PasswordLengthException

    password_set = set(password)
    password_allowed_symbols = set(AllowedSymbols.PASSWORD_ALLOWED_SYMBOLS.value)
    if len(password_set - password_allowed_symbols) > 0:
        raise PasswordDisallowedSymbolsException


def check_registration(request) -> dict[str, str, str, str]:
    print(request)
    if "username" in request:
        is_username_accepted(str(request["username"]))
    else:
        raise UsernameNotInRequestException
    print("check registration1")
    if "forname" in request:
        is_forname_accepted(str(request["forname"]))
    else:
        raise FornameNotInRequestException

    if "surname" not in request:
        is_surname_accepted(str(request["surname"]))
    else:
        raise SurnameNotInRequestException

    if "password" not in request:
        is_password_accepted(str(request["password"]))
    else:
        raise PasswordNotInRequestException

    return {
        "username": str(request["username"]),
        "forname": str(request["forname"]),
        "surename": str(request["surname"]),
        "password": str(request["password"]),
    }
