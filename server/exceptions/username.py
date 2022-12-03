# Username
class UsernameNotInRequestException(Exception):
    pass


class UsernameExistsAlreadyException(Exception):
    pass


class UsernameLengthException(Exception):
    pass


class UsernameDisallowedSymbolsException(Exception):
    pass