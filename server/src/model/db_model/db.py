from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


def initialize_db(app: Flask) -> None:
    db.init_app(app)
    db.create_all()
