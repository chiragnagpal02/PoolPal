from flask import Blueprint, render_template, request, jsonify
from src.databases import Passengers, db

passenger = Blueprint('passenger', __name__, url_prefix='/api/passenger')


@passenger.route('/get_all_passengers')
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

@passenger.route('/get_passenger_by_id/<passenger_id>')
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

@passenger.route('/get_passenger_by_username/<username>')
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


@passenger.route('/add_new_passenger', methods=['POST'])
def add_new_passenger():
    PUserName = request.json['PUserName']
    PAge = request.json['PAge']
    PGender = request.json['PGender']
    PEmail = request.json['PEmail']
    PPhone = request.json['PPhone']

    new_passenger = Passengers(
        PUserName=PUserName, 
        PAge=PAge,
        PGender=PGender, 
        PEmail=PEmail, 
        PPhone=PPhone
        )
    
    db.session.add(new_passenger)
    db.session.commit()
    return jsonify(
        {
            "code": 200,
            "data": {
                "Status": f"New passenger with ID {new_passenger.PID} has been added."
            }
        }
    )


'''
PName = db.Column(db.String(200), nullable=False)
    PUserName = db.Column(db.String(200), nullable=False, unique=True)
    PAge = db.Column(db.Integer, nullable=False)
    PGender = db.Column(db.String(1), nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)
    PAddress = db.Column(db.String(400), nullable=False)
    PPhone = db.Column(db.Integer, nullable=False)
    PAccount_Created_At = db.Column(db.DateTime, default=datetime.now())

'''