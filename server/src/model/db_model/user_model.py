from src.model.db_model.db import db
from uuid import uuid4
from src.enum.roles import Role
from flask_bcrypt import generate_password_hash, check_password_hash


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, nullable=False, default=get_uuid)
    username = db.Column(db.String(20), unique=True, nullable=False)
    forname = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.User.value)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f"<User @{self.username} | {self.forname.capitalize()} {self.surname.capitalize()} is {self.role.value}>"
