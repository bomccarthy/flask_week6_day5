from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, firstname, lastname, username, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def modify(self, firstname, lastname, username, email, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        db.session.commit()
    
    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, user_id, name, date_created):
        self.user_id = user_id
        self.name = name
        self.date_created = date_created

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()        