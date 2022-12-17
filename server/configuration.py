from datetime import timedelta
from dotenv import load_dotenv
import os
import redis

load_dotenv()


class DevelopmentConfiguration:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    # SPOTIFY
    # SPOTIPY_REDIRECT_URI = "http://localhost:9000"
    # SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
    # SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

    # SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = r"sqlite:///main.sqlite"

    # SESSION
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    SESSION_COOKIE_HTTPONLY = (True,)
    REMEMBER_COOKIE_HTTPONLY = (True,)
    SESSION_COOKIE_SAMESITE = "Strict"
