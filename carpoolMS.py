from functools import wraps
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import validators
from datetime import datetime
import jwt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Carpool(db.Model):
    __tablename__ = 'carpooling'

    CPID = db.Column(db.Integer, autoincrement=True)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    DriverFee = db.Column(db.Float(precision=2), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    CPStartLocation = db.Column(db.String(64), nullable=False)
    CPStartCoordinates = db.Column(db.Float(precision=10), nullable=False)
    CPendLocation = db.Column(db.String(64), nullable=False)
    CPEndCoordinates = db.Column(db.Float(precision=10), nullable=False)
    Status = db.Column(db.String(64), nullable=False)
    Capacity_remaining = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DID'),
        {},
    )

    def __init__(self, CPID, DID, DriverFee, DateTime, CPStartLocation, CPStartCoordinates, CPendLocation, CPendCoordinates, Status, Capacity_remaining):
        self.CPID = CPID
        self.DID = DID
        self.DriverFee = DriverFee
        self.DateTime = DateTime
        self.CPStartLocation = CPStartLocation
        self.CPStartCoordinates = CPStartCoordinates
        self.CPendLocation = CPendLocation
        self.CPendCoordinates = CPendCoordinates
        self.Status = Status
        self.Capacity_remaining = Capacity_remaining

    def json(self):
        return {
            "CPID": self.CPID,
            "DID": self.DID,
            "DriverFee": self.DriverFee,
            "DateTime": self.DateTime,
            "CPStartLocation": self.CPStartLocation,
            "CPStartCoordinates": self.CPStartCoordinates,
            "CPendLocation": self.CPendLocation,
            "CPendCoordinates": self.CPendCoordinates,
            "Status": self.Status,
            "Capacity_remaining": self.Capacity_remaining
        }
    
class Carpeople(db.Model):
    __tablename__ = 'carpeople'

    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), autoincrement=True)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passenger.PID'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DID', 'PID'),
    )

    def __init__(self, CPID, DID, PID):
        self.CPID = CPID
        self.DID = DID
        self.PID = PID
    
    def json(self):
        return {
            "CPID": self.CPID,
            "DID": self.DID,
            "PID": self.PID
        }
    

@app.route('/api/v1/carpool/add_new_carpool', methods=['POST'])
def add_new_passenger():
    DID = request.json.get('DID')
    DriverFee = request.json.get('DriverFee')
    CPStartLocation = request.json.get('CPStartLocation')
    CPStartCoordinates = request.json.get('CPStartCoordinates')
    CPendLocation = request.json.get('CPendLocation')
    CPendCoordinates = request.json.get('CPendCoordinates')
    Status = request.json.get('Status')
    Capacity_remaining = request.json.get('Capacity_remaining')

    new_carpool = Carpool(
        DID=DID, 
        DriverFee=DriverFee,
        CPStartLocation=CPStartLocation,
        CPStartCoordinates=CPStartCoordinates,
        CPendLocation=CPendLocation,
        CPendCoordinates=CPendCoordinates,
        Status=Status,
        Capacity_remaining=Capacity_remaining
    )

    db.session.add(new_carpool)
    db.session.commit()

    return jsonify({
        "code": 200,
        "data": {
            "status": f"New passenger with ID {new_carpool.CPID} has been added."
        }
    })

@app.route('/get_all_carpools', methods=['GET'])
def get_all_carpools():
    carpools = Carpool.query.all()
    return jsonify({
        "code": 200,
        "data": {
            "carpools": [carpool.json() for carpool in carpools]
        }
    }), 200


@app.route('/update_carpool_capacity/<CPID>', methods=['PUT'])
def update_carpool_capacity(CPID):
    CPID = int(CPID)
    carpool = Carpool.query.filter_by(CPID=CPID).first()
    capacity = carpool.Capacity_remaining
    # check if the exising capacity is greater than 0. only then subtract. else return the error - 
    # capacity cannot be negative.
    if capacity > 0:
        capacity = capacity - 1
        carpool.Capacity_remaining = capacity
        db.session.commit()
        return jsonify({
            "code": 200,
            "data": {
                "status": f"Capacity of carpool {CPID} has been updated."
            }
        }), 200
    else:
        return jsonify({
            "code": 400,
            "data": {
                "status": f"Carpool with {CPID} is already full! Cannot add more people"
            }
        }), 400




if __name__ == '__main__':
    app.run(debug=True, port=5000)



    