from flask import Blueprint, jsonify, request
from src.database import Carpool, db
from constants.http_status_codes import *


carpool = Blueprint('carpool', __name__, url_prefix='/api/v1/carpool')


@carpool.route('/register', methods=['POST'])
def create_carpool():
    did = request.json['DID']
    pid = request.json['PID']
    startlocationlat = request.json["Start_Location_Lat"]
    startlocationlong = request.json["Start_Location_Long"]
    endlocationlat = request.json["End_Location_Lat"]
    endlocationlong = request.json["End_Location_Long"]
    distance = request.json["Distance"]
    datetime = request.json["Date_Time"]
    availableseats = request.json["Available_Seats"]
    price = request.json["Price"]
    status = request.json["Status"]
    
    new_carpool = Carpool(
        DID = did,
        PID = pid,
        Start_Location_Lat = startlocationlat,
        Start_Location_Long = startlocationlong,
        End_Location_Lat = endlocationlat,
        End_Location_Long = endlocationlong,
        Distance = distance,
        Date_Time = datetime,
        Available_Seats = availableseats,
        Price = price,
        Status = status,
    
    )

    db.session.add(new_carpool)
    db.session.commit()
    
    return jsonify({
        "message": "Carpool created successfully",
        'carpool': {
            
            }
        }), HTTP_201_CREATED

    # return {'message': 'User Created'}


@carpool.route('/me')
def me():
    return {'message': 'User Me'}
