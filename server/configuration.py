from dotenv import load_dotenv
import os

load_dotenv()


class DevelopmentConfiguration:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    # SPOTIFY
    SPOTIPY_REDIRECT_URI = "http://localhost:9000"
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

    # SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = r"sqlite:///main.sqlite"

    # SESSION
    SESSION_TYPE = "mongodb"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_MONGODB_DB = 'session_storage'
