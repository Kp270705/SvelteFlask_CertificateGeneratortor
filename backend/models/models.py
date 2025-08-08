# Project/Backend/models/models.py

from initResources.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # hash is long, so use 128

    details = db.relationship('UserDetails', backref='user', uselist=False, cascade="all, delete-orphan")

    def __init__(self, email, password):
        self.email = email
        self.password = password


class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(120), nullable=True)
    userHobbies = db.Column(db.String(120), nullable=True)
    socialMediaLink = db.Column(db.Text, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    def __init__(self, user_id, userName=None, userHobbies=None, socialMediaLink=None):
        self.user_id = user_id
        self.userName = userName
        self.userHobbies = userHobbies
        self.socialMediaLink= socialMediaLink
