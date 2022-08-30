from flask_bcrypt import generate_password_hash, check_password_hash
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Resource, Api

# from myproject import db, app


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(64), index=True)

    def __int__(self, username, email, password, img_url):
        self.username = username
        self.email = email
        self.password_hash = password
        self.img_url = img_url

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def json(self):
        password = str(self.password_hash)
        return {'username': self.username, 'email': self.email, 'password': password,
                'image_url': self.image_url}

    def __repr__(self):
        return f"Username: {self.username}"


class Professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64), index=True)
    calendly_url = db.Column(db.String(64), index=True)
    skill_level = db.Column(db.String(64), index=True)
    category = db.Column(db.String(64), index=True)
    bio = db.Column(db.String(64), index=True)
    specialization = db.Column(db.String(64), index=True)

    def __init__(self, username, email, password, calendly_url, skill_level, bio, category, specialization):
        self.username = username
        self.email = email
        self.password_hash = password
        self.calendly_url = calendly_url
        self.skill_level = skill_level
        self.bio = bio
        self.category = category
        self.specialization = specialization

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def json(self):
        password = str(self.password_hash)
        return {'username': self.username, 'email': self.email, 'password': password,
                'calendly_url': self.calendly_url, 'skill_level': self.skill_level, 'bio': self.bio,
                'category': self.category, 'specialization': self.specialization}

    def __repr__(self):
        return f"Username: {self.username}"
