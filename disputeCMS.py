from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

DRIVER_URL = 'http://127.0.0.1:5000/api/v1/driver/get_all_drivers'
PASSENGER_URL = 'http://127.0.0.1:5001/api/v1/get_all_passengers'
STAFF_URL = 'http://127.0.0.1:5007/staff'

class Dispute(db.Model):
    __tablename__ = 'dispute'

    disputeID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    CPID = db.Column(db.Integer, nullable=False)
    PID = db.Column(db.Integer, nullable=False)
    DID = db.Column(db.Integer, nullable=False)

    def __init__(self, amount, CPID, PID, DID):
            self.amount = amount
            self.CPID = CPID
            self.PID = PID
            self.DID = DID

    def json(self):
        return {
            "disputeID": self.disputeID,
            "amount": self.amount,
            "CPID": self.CPID,
            "PID": self.PID,
            "DID": self.DID,
            }

@app.route('/api/v1/dispute/create_dispute/<int:amount>/<int:CPID>/<int:PID>/<int:DID>', methods=['POST'])
def create_dispute(amount,CPID,PID,DID):
    #id = request.get_json()['id']
    amount = amount
    CPID = CPID
    PID = PID
    DID = DID
    
    new_dispute = Dispute(
        amount,
        CPID,
        PID,
        DID
    )

    db.session.add(new_dispute)
    db.session.commit()

    return jsonify(
         {
        "code": 201,
        "data": new_dispute.json()
        }
    ), 201


def get_existing_driverDetails():
    response = requests.get(DRIVER_URL)
    driverID = response.json()['data']['Driver']
    for i in driverID:
        dID = i['DID']
        dName = i['DName']
        dVeh = i['DVehicleNo']
        dNo = i['DPhoneNo'] 


def get_existing_PassengerDetails():
    response = requests.get(PASSENGER_URL)
    passengerID = response.json()['data']['Passengers']
    for i in passengerID:
        pID = i['PID']
        pName = i['PName']
        dNo = i['PPhone'] 

def staffDetails():
    response = requests.get(PASSENGER_URL)
    staffID = response.json()['data']['Staff']
    for i in staffID:
        sID = i['SID']
        sName = i['SName']


if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=5125)

