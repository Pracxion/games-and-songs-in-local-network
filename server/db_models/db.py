from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
def initialize_db(app):
    db.init_app(app)
    # Create Database Models
    db.create_all()