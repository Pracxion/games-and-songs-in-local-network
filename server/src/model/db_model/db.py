import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()


def initialize_db(app: Flask) -> None:
    print(os.getcwd())
    db.init_app(app)
    # Create Database Models
    db.create_all()
