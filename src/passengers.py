from flask import Blueprint, jsonify, request
from src.database import Passengers, db

from constants.http_status_codes import *

passengers = Blueprint('passengers', __name__, url_prefix='/api/v1/passengers')


@passengers.route('/create', methods=['POST'])
def create_passenger():
    pname = request.json['PName']
    page = request.json['PAge']
    pgender = request.json['PGender']
    pemail = request.json['PEmail']
    paddress = request.json['PAddress']
    pphone = request.json['PPhone']


    new_passenger = Passengers(
        PName=pname,
        PAge=page,
        PGender=pgender,
        PEmail=pemail,
        PAddress=paddress,
        PPhone=pphone,
        
    )

    db.session.add(new_passenger)
    db.session.commit()
    
    return jsonify({
        "message": "Passenger created successfully",
        'passenger': {
            'Passenger Name': new_passenger.PName,
            'Passenger Age': new_passenger.PAge,
            'Passenger Gender': new_passenger.PGender,
            'Passenger Email': new_passenger.PEmail,
            'Passenger Address': new_passenger.PAddress,
            'Passenger Phone': new_passenger.PPhone,
            
            }
        }), HTTP_201_CREATED


@passengers.route('/me')
def me():
    return {'message': 'User Me'}
