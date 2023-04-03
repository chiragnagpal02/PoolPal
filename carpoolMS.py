# from functools import wraps
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
# import validators
from datetime import datetime
# # import jwt
# import uuid


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:8889/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Carpool(db.Model):
    __tablename__ = 'carpooling'

    CPID = db.Column(db.Integer, autoincrement=True)
    DID = db.Column(db.Integer, nullable=False)
    CarpoolPrice = db.Column(db.Float(precision=2), nullable=False)
    PassengerPrice = db.Column(db.Float(precision=2), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    CPStartLocation = db.Column(db.String(64), nullable=False)
    CPStartLatitude = db.Column(db.Float(precision=10), nullable=False)
    CPStartLongitude = db.Column(db.Float(precision=10), nullable=False)
    CPEndLocation = db.Column(db.String(64), nullable=False)
    CPEndLatitude = db.Column(db.Float(precision=10), nullable=False)
    CPEndLongitude = db.Column(db.Float(precision=10), nullable=False)
    Status = db.Column(db.String(64), nullable=False)
    Capacity_remaining = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DID'),
        {},
    )

    def __init__(self, CarpoolPrice, PassengerPrice, CPID, DID, DriverFee, DateTime, CPStartLatitude, CPStartLongitude ,CPStartLocation, CPEndLocation, CPEndLatitude, CPEndLongitude ,Status, Capacity_remaining):
        self.CPID = CPID
        self.DID = DID
        self.CarpoolPrice = CarpoolPrice
        self.PassengerPrice = PassengerPrice
        self.DateTime = DateTime
        self.CPStartLatitude = CPStartLatitude
        self.CPStartLongitude = CPStartLongitude
        self.CPStartLocation = CPStartLocation
        self.CPEndLocation = CPEndLocation
        self.CPEndLatitude = CPEndLatitude
        self.CPEndLongitude = CPEndLongitude
        self.Status = Status
        self.Capacity_remaining = Capacity_remaining

    def json(self):
        return {
            "CPID": self.CPID,
            "DID": self.DID,
            "DateTime": self.DateTime,
            "CarpoolPrice": self.CarpoolPrice,
            "PassengerPrice": self.PassengerPrice,
            "CPStartLocation": self.CPStartLocation,
            "CPStartLatitude": self.CPStartLatitude,
            "CPStartLongitude": self.CPStartLongitude,
            "CPEndLocation": self.CPEndLocation,
            "CPEndLatitude": self.CPEndLatitude,
            "CPEndLongitude": self.CPEndLongitude,
            "Status": self.Status,
            "Capacity_remaining": self.Capacity_remaining
        }

@app.route('/api/v1/carpool/add_new_carpool', methods=['POST'])
def add_new_passenger():
    DID = request.json.get('DID')
    CarpoolPrice = request.json.get('CarpoolPrice')
    DriverFee = request.json.get('DriveFee')
    PassengerPrice = request.json.get('PassengerPrice')
    DateTime = request.json.get('DateTime')
    CPStartLocation = request.json.get('CPStartLocation')
    CPStartLatitude = request.json.get('CPStartLatitude')
    CPStartLongitude = request.json.get('CPStartLongitude')
    CPEndLatitude = request.json.get('CPEndLatitude')
    CPEndLongitude = request.json.get('CPEndLongitude')
    CPEndLocation = request.json.get('CPEndLocation')
    Status = request.json.get('Status')
    Capacity_remaining = request.json.get('Capacity_remaining')
    
    # Generate a unique ID
    # new_cpid = str(uuid.uuid4())
    
    new_carpool = Carpool(
        DID=DID, 
        CarpoolPrice=CarpoolPrice,
        DriverFee = DriverFee,
        PassengerPrice=PassengerPrice,
        DateTime = DateTime,
        CPStartLocation=CPStartLocation,
        CPStartLatitude=CPStartLatitude,
        CPStartLongitude=CPStartLongitude,
        CPEndLocation=CPEndLocation,
        CPEndLatitude=CPEndLatitude,
        CPEndLongitude=CPEndLongitude,
        Status=Status,
        Capacity_remaining=Capacity_remaining
    )

    db.session.add(new_carpool)
    db.session.commit()

    return jsonify({
        "code": 200,
        "data": {
            "status": f"New Carpool with ID {new_carpool.CPID} has been added."
        }
    })

@app.route('/api/v1/carpool/get_all_carpools', methods=['GET'])
def get_all_carpools():
    carpools = Carpool.query.all()
    return jsonify({
        "code": 200,
        "data": {
            "carpools": [carpool.json() for carpool in carpools]
        }
    }), 200

@app.route('/api/v1/carpool/get_carpool_by_id/<CPID>', methods=['GET'])
def get_carpool_by_id(CPID):
    CPID = int(CPID)
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    
    if carpool is None:
        return jsonify({
            "code": 404,
            "data": {
                "message": "Carpool not found"
            }
        }), 404
    
    return jsonify({
        "code": 200,
        "data": {
            "carpool": carpool.json()
        }
    }), 200

@app.route('/api/v1/carpool/get_carpool_by_driver_id/<DID>', methods=['GET'])
def get_carpool_by_driver_id(DID):
    DID = int(DID)
    carpools = Carpool.query.filter_by(DID=DID).all()
    return jsonify({
        "code": 200,
        "data": {
            "carpools": [carpool.json() for carpool in carpools]
        }
    }), 200

@app.route('/api/v1/carpool/get_carpool_by_passenger_id/<PID>', methods=['GET'])
def get_carpool_by_passenger_id(PID):
    PID = int(PID)
    carpools = Carpool.query.filter_by(PID=PID).all()
    return jsonify({
        "code": 200,
        "data": {
            "carpools": [carpool.json() for carpool in carpools]
        }
    }), 200

@app.route('/api/v1/carpool/update_carpool_capacity/<CPID>', methods=['PUT'])
def update_carpool_capacity(CPID):
    CPID = int(CPID)
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    capacity = carpool.Capacity_remaining
    # check if the exising capacity is greater than 0. only then subtract. else return the error - 
    # capacity cannot be negative.
    capacity = capacity - 1
    carpool.Capacity_remaining = capacity
    db.session.commit()
    return jsonify({
        "code": 200,
        "data": {
            "status": f"Capacity of carpool {CPID} has been updated."
        }
    }), 200
    
# do we still need this????
@app.route("/api/v1/carpool/update_passenger_price/<CPID>", methods=['PUT'])
def update_passenger_price(CPID):
    CPID = int(CPID)
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    carpool.CarpoolPrice = request.json.get('PassengerPrice')
    db.session.commit()
    return jsonify({
        "code": 200,
        "data": {
            "status": f"Passenger price of carpool {CPID} has been updated."
        }
    }), 200

# update status to "Not Active"
@app.route("/api/v1/carpool/update_carpool_status/<CPID>", methods=['PUT'])
def update_carpool_status(CPID):
    CPID = int(CPID)
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    carpool.Status = "Not Active"
    db.session.commit()
    return jsonify({
        "code": 200,
        "data": {
            "status": f"Carpool {CPID} status has been updated."
        }
    }), 200

# delete carpool
@app.route("/api/v1/carpool/remove_carpool/<CPID>", methods=['DELETE'])
def remove_carpool(CPID):
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    if carpool:
        db.session.delete(carpool)
        db.session.commit()
        return jsonify(
            {
                'code': 200,
                'message': f'Carpool has been removed'
            }
        ), 200
    
    else:
        return jsonify({
            "code": 404,
            "message": "The carpool does not exist."
        }), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5002)

