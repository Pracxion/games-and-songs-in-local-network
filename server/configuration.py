from configparser import ConfigParser
import pathlib
from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:

    APP_SECRET_KEY = os.environ.get("SECRET_KEY")

    # [SPOTIFY]
    SPOTIPY_REDIRECT_URI = "http://localhost:9000"
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

    SPOTIFY_SCOPES = {
        "USER_READ_PLAYBACK_STATE": "user-read-playback-state",
        "USER_MODIFY_PLAYBACK_STATE": "user-modify-playback-state",
        "PLAYLIST_MODIFY_PUBLIC": "playlist-modify-public",
        "PLAYLIST_MODIFY_PRIVATE": "playlist-modify-private",
        "USER_READ_RECENTLY_PLAYED": "user-read-recently-played",
        "USER_READ_PLAYBACK_POSITION": "user-read-playback-position",
        "PLAYLIST_READ_PRIVATE": "playlist-read-private",
        "USER_LIBRARY_MODIFY": "user-library-modify",
        "USER_READ_CURRENTLY_PLAYING": "user-read-currently-playing",
    }

    # [SQLALCHEMY]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///../database/main.sqlite"

    # [REGISTRATION]
    USERNAME_ALLOWED_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_"
    NAME_ALLOWED_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz -"
    PASSWORD_ALLOWED_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !#$%&()*+,-./:;<=>?@[]^_`{|}~"

    # [SESSION]
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = ""  # redis.from_url("redis")
