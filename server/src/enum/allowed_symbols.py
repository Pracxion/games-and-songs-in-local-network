from enum import Enum


class AllowedSymbols(Enum):
    USERNAME_ALLOWED_SYMBOLS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_"
    NAME_ALLOWED_SYMBOLS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -"
    PASSWORD_ALLOWED_SYMBOLS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !#$%&()*+,-./:;<=>?@[]^_`{|}~"
