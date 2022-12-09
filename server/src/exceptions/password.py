# Password
class PasswordNotInRequestException(Exception):
    pass


class PasswordLengthException(Exception):
    pass


class PasswordDisallowedSymbolsException(Exception):
    pass