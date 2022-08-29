from flask_bcrypt import generate_password_hash, check_password_hash
from __init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64), index=True)
    image_url = db.Column(db.String(64), index=True)

    def __int__(self, username, email, password, img_url):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.img_url = img_url

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
        self.password_hash = generate_password_hash(password)
        self.calendly_url = calendly_url
        self.skill_level = skill_level
        self.bio = bio
        self.category = category
        self.specialization = specialization

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username}"
