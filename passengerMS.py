from functools import wraps
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from authenticationMS import login_is_required
import validators
import bcrypt
from datetime import datetime
import jwt


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/PoolPal'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Passengers(db.Model):
    __tablename__ = 'passengers'
    
    PID = db.Column(db.Integer, autoincrement=True)
    PName = db.Column(db.String(200), nullable=False)
    PUserName = db.Column(db.String(200), nullable=False, unique=True)
    PAge = db.Column(db.Integer, nullable=False)
    PGender = db.Column(db.String(1), nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)
    PAddress = db.Column(db.String(400), nullable=False)
    PPhone = db.Column(db.Integer, nullable=False)
    PAccount_Created_At = db.Column(db.DateTime, default=datetime.now())

    __table_args__ = (
        db.PrimaryKeyConstraint('PID', 'PEmail'),
        {},
    )

    def __init__(self, PName, PUserName, PAge, PGender, PEmail, PAddress, PPhone, PAccount_Created_At):
        self.PName = PName
        self.PUserName = PUserName
        self.PAge = PAge
        self.PGender = PGender
        self.PEmail = PEmail
        self.PAddress = PAddress
        self.PPhone = PPhone
        self.PAccount_Created_At = PAccount_Created_At

    def json(self):
        return {
            "PID": self.PID,
            "PName": self.PName,
            "PUserName": self.PUserName,
            "PAge": self.PAge,
            "PGender": self.PGender,
            "PEmail": self.PEmail,
            "PAddress": self.PAddress,
            "PPhone": self.PPhone,
            "PAccount_Created_At": self.PAccount_Created_At
        }
    
@app.route('/')
def home():
    return "Hi World"

@app.route('/api/v1/get_all_passengers')
def get_all_passengers():
    passengers = Passengers.query.all()
    if len(passengers):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "passengers": [passenger.json() for passenger in passengers]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no passengers."
        }
    ), 404

@app.route('/api/v1/get_passenger_by_id/<passenger_id>')
def get_passenger_by_id(passenger_id):
    passenger = Passengers.query.filter_by(PID=passenger_id).first()
    if passenger:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "passenger": passenger.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"There is no passenger with passenger ID : {passenger_id}."
        }
    ), 404

@app.route('/get_passenger_by_username/<username>')
def get_passenger_by_username(username):
    passenger = Passengers.query.filter_by(PUserName=username).first()
    if passenger:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "passenger": passenger.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"There is no passenger with username {username}!"
        }
    ), 404


@app.route('/api/v1/add_new_passenger', methods=['POST'])
def add_new_passenger():
    PName = request.json.get('PName')
    PUserName = request.json.get('PUserName')
    PAge = request.json.get('PAge')
    PGender = request.json.get('PGender')
    PEmail = request.json.get('PEmail')
    PAddress = request.json.get('PAddress')
    PPhone = request.json.get('PPhone')
    PAccount_Created_At = datetime.now()

    # Check if a passenger with the same email address already exists
    existing_passenger = Passengers.query.filter_by(PEmail=PEmail).first()
    if existing_passenger:
        return jsonify({
            "code": 400,
            "message": "A passenger with this email address already exists."
        }), 400

    # Validate email address
    if not validators.email(PEmail):
        return jsonify({
            "code": 400,
            "message": "Invalid email.",
            "email": f"{PEmail} is not a valid email."
        }), 400

    new_passenger = Passengers(
        PName,
        PUserName,
        PAge,
        PGender,
        PEmail,
        PAddress,
        PPhone,
        PAccount_Created_At
    )

    db.session.add(new_passenger)
    db.session.commit()

    return jsonify({
        "code": 200,
        "data": {
            "status": f"New passenger with ID {new_passenger.PID} has been added."
        }
    })

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True, port=5001)