from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import stripe
from invokes import invoke_http

import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)

PAYMENTLOG_URL = "http://127.0.0.1:5055/api/v1/paymentlog/get_CPID_PID/"

stripe_keys = {
  'secret_key': 'sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR',
  'publishable_key': 'pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh'
}

stripe.api_key = stripe_keys["secret_key"]

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

@app.route("/api/v1/paymentlogs/add_new_payment_log/<session_id>/<CPID>/<PID>", methods=['POST'])
def retrievefromStripe(session_id,CPID,PID):
    # Retrieve the Checkout Session
    session_id_str = session_id
    CPID_str = CPID
    PID_str = PID
    checkout_session = stripe.checkout.Session.retrieve(session_id_str)
    amount = checkout_session["amount_total"] / 100
    #print(create_payment(checkout_session["payment_intent"],session_id_str,amount,CPID_str,PID_str,checkout_session["payment_status"]))
    logs = PaymentLogs1('',checkout_session["payment_intent"],session_id_str,amount,CPID_str,PID_str,checkout_session["payment_status"])

    try:
        db.session.add(logs)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the log."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            #"data": PaymentLogs.json()
        }
    ), 201

@app.route("/api/v1/paymentlogs/add_new_refund_log/<string:IntentID>", methods=['POST'])
def create_refund_log(IntentID):
    #IntentID = intent_id["intent_id"]
    intent = stripe.PaymentIntent.retrieve(IntentID)
    #print(intent)
    Amount = intent["amount"]/100
    Status = intent["status"]
    URL = PAYMENTLOG_URL + IntentID
    result = invoke_http(URL, method='GET')
    sessionID = result["data"]["sessionID"]
    CPID = result["data"]["CPID"]
    PID = result["data"]["PID"]
    logs = PaymentLogs1('',IntentID,sessionID,Amount,CPID,PID,Status)

    try:
        db.session.add(logs)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the log."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            #"data": PaymentLogs.json()
        }
    ), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5055)