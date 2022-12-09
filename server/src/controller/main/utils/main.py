from flask import request
from src.exceptions.forname import FornameDisallowedSymbolsException, FornameLengthException, FornameNotInRequestException
from src.exceptions.surname import SurnameDisallowedSymbolsException, SurnameLengthException, SurnameNotInRequestException
from src.exceptions.password import PasswordDisallowedSymbolsException, PasswordLengthException, PasswordNotInRequestException
from src.exceptions.username import (
    UsernameDisallowedSymbolsException,
    UsernameExistsAlreadyException,
    UsernameLengthException,
    UsernameNotInRequestException,
)
from src.model.db_model.user_model import User
from src.enum.allowed_symbols import AllowedSymbols


def is_username_accepted(request) -> None:

    if "username" in request:
        username = str(request["username"])
    else:
        raise UsernameNotInRequestException

    if not 3 <= len(username) <= 20:
        raise UsernameLengthException

    username_set = set(username)
    username_allowed_symbols = set(AllowedSymbols.USERNAME_ALLOWED_SYMBOLS.value)
    if len(username_set - username_allowed_symbols) > 0:
        raise UsernameDisallowedSymbolsException

    check_if_user_exist = User.query.filter_by(username=username).first()
    print(check_if_user_exist)
    if check_if_user_exist is not None:
        raise UsernameExistsAlreadyException


def is_forname_accepted(request) -> None:

    if "forname" in request:
        forname = str(request["forname"])
    else:
        raise FornameNotInRequestException

    if not 3 <= len(forname) <= 20:
        raise FornameLengthException

    forname_set = set(forname)
    forname_allowed_symbols = set(AllowedSymbols.NAME_ALLOWED_SYMBOLS.value)
    if len(forname_set - forname_allowed_symbols) > 0:
        raise FornameDisallowedSymbolsException


def is_surname_accepted(request) -> None:

    if "surname" in request:
        surname = str(request["surname"])
    else:
        raise SurnameNotInRequestException

    if not 3 <= len(surname) <= 20:
        raise SurnameLengthException

    surname_set = set(surname)
    surname_allowed_symbols = set(AllowedSymbols.NAME_ALLOWED_SYMBOLS.value)
    if len(surname_set - surname_allowed_symbols) > 0:
        raise SurnameDisallowedSymbolsException


def is_password_accepted(request) -> None:

    if "password" in request:
        password = str(request["password"])
    else:
        raise PasswordNotInRequestException

    if not 6 <= len(password):
        raise PasswordLengthException

    password_set = set(password)
    password_allowed_symbols = set(AllowedSymbols.PASSWORD_ALLOWED_SYMBOLS.value)
    if len(password_set - password_allowed_symbols) > 0:
        raise PasswordDisallowedSymbolsException


def check_registration(request) -> dict[str, str, str, str]:
    is_username_accepted(request)
    is_forname_accepted(request)
    is_surname_accepted(request)
    is_password_accepted(request)
    print("Geschafft\n\n\n\n\n\n\n\n")
    return {
        "username": str(request["username"]),
        "forname": str(request["forname"]),
        "surname": str(request["surname"]),
        "password": str(request["password"]),
    }
