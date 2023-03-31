from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import amqp_setup
import pika
import json
import stripe

from invokes import invoke_http

import json
import os

import amqp_setup

monitorBindingKey='*.payment'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)

# Set your secret key
stripe_keys = {
  'secret_key': 'sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR',
  'publishable_key': 'pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh'
}

stripe.api_key = stripe_keys["secret_key"]

class PaymentLogs(db.Model):
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
            "ID": self.ID,
            "intentID": self.intentID,
            "sessionID": self.sessionID,
            "Amount" : self.Amount,
            "CPID" : self.CPID,
            "PID" : self.PID,
            "Status" : self.Status

        }

def receivePaymentLog():
    amqp_setup.check_setup()
        
    queue_name = 'Payment_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an payment log by " + __file__)
    processPaymentLog(json.loads(body))
    print() # print a new line feed

def processPaymentLog(session_id):
    print("Recording an payment log:")
    print(session_id)
    retrievefromStripe(session_id)
    #print(create_payment(order))

def retrievefromStripe(session_id):
    # Retrieve the Checkout Session
    session_id_str = str(session_id["session_id"])
    CPID_str = str(session_id["CPID"])
    PID_str = str(session_id["PID"])
    checkout_session = stripe.checkout.Session.retrieve(session_id_str)
    amount = checkout_session["amount_total"] / 100
    print(create_payment(checkout_session["payment_intent"],session_id_str,amount,CPID_str,PID_str,checkout_session["payment_status"]))


@app.route("/api/v1/paymentlogs/add_new", methods=['POST'])
def create_payment(intentID,sessionID,Amount,CPID,PID,Status):
    logs = PaymentLogs('',intentID,sessionID,Amount,CPID,PID,Status)

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

@app.route("/api/v1/paymentlogs/get_paymentlogs_by_intent_id/<int:intentID>")
def find_by_id(intentID):
    payment = PaymentLogs.query.filter_by(intentID=intentID).first()
    if payment:
        return jsonify(
            {
                "code": 200,
                "data": payment.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Payment Log not found."
        }
    ), 404

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receivePaymentLog()