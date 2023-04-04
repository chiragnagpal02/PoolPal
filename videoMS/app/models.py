from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('access denied')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return dict(id=self.id,
                    username=self.username,
                    email=self.email)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    feedback_description = db.Column(db.String(256))

    def __init__(self, name, email, phone_number, rating, feedback_description):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.rating = rating
        self.feedback_description = feedback_description


    def json(self):
        return {
            "name": self.name,
            "email": self.email, 
            "phone_number": self.phone_number, 
            "rating": self.rating, 
            "feedback_description": self.feedback_description
        }