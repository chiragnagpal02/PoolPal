from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import stripe

import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)

class PaymentLogs1(db.Model):
    __tablename__ = 'paymentlogs'
    
    logsID = db.Column(db.Integer, autoincrement=True)
    intentID = db.Column(db.String(200), nullable=False)
    sessionID = db.Column(db.String(200), nullable=False)
    Amount = db.Column(db.Integer, nullable=False)
    CPID = db.Column(db.Integer, nullable=False)
    PID = db.Column(db.Integer, nullable=False)
    Status = db.Column(db.String(64), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('logsID'),
        {},
    )

    def __init__(self, logsID, intentID, sessionID, Amount, CPID, PID, Status):
        self.logsID = logsID
        self.intentID = intentID
        self.sessionID = sessionID
        self.Amount = Amount
        self.CPID = CPID
        self.PID = PID
        self.Status = Status

    def json(self):
        return {
            "logsID": self.logsID,
            "intentID": self.intentID,
            "sessionID": self.sessionID,
            "Amount" : self.Amount,
            "CPID" : self.CPID,
            "PID" : self.PID,
            "Status" : self.Status

        }
    
@app.route("/api/v1/paymentlog/get_intent_by_ID/<int:CPID>/<int:PID>")
def find_by_CPID_PID(CPID,PID):
    data = {
        "CPID" : CPID,
        "PID" : PID
    }
    paymentlog = PaymentLogs1.query.filter_by(**data).first()
    if paymentlog:
        return jsonify(
            {
                "code": 200,
                "data": paymentlog.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment log not found."
        }
    ), 404

@app.route("/api/v1/paymentlog/get_CPID_PID/<string:intent_id>")
def find_by_intent_id(intent_id):
    paymentlog = PaymentLogs1.query.filter_by(intentID=intent_id).first()
    if paymentlog:
        return jsonify(
            {
                "code": 200,
                "data": paymentlog.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment log not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5055)