# Username
class UsernameNotInRequestException(Exception):
    pass


class UsernameExistsAlreadyException(Exception):
    pass


class UsernameLengthException(Exception):
    pass


class UsernameDisallowedSymbolsException(Exception):
    pass


# Forename
class ForenameNotInRequestException(Exception):
    pass


class ForenameLengthException(Exception):
    pass


class ForenameDisallowedSymbolsException(Exception):
    pass


# Surename
class SurenameNotInRequestException(Exception):
    pass


class SurenameLengthException(Exception):
    pass


class SurenameDisallowedSymbolsException(Exception):
    pass


# Password
class PasswordNotInRequestException(Exception):
    pass


class PasswordLengthException(Exception):
    pass


class PasswordDisallowedSymbolsException(Exception):
    pass
