from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import amqp_setup
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

PAYMENTLOG_URL = "http://127.0.0.1:5055/api/v1/paymentlog/get_CPID_PID/"

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
            "logsID": self.logsID,
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
    routing_key = method.routing_key
    print("Received a message with routing key:", routing_key)
    if (routing_key == "create.payment") :
        processPaymentLog(json.loads(body))
    else :
        processRefundLog(json.loads(body))
    print() # print a new line feed

def processPaymentLog(session_id):
    print("Recording an payment log:")
    print(session_id)
    retrievefromStripe(session_id)
    #print(create_payment(order))

def processRefundLog(intent_id):
    print("Recording a refund log:")
    print(intent_id)
    retrieverefundfromStripe(intent_id)

def retrievefromStripe(session_id):
    # Retrieve the Checkout Session
    session_id_str = str(session_id["session_id"])
    CPID_str = str(session_id["CPID"])
    PID_str = str(session_id["PID"])
    checkout_session = stripe.checkout.Session.retrieve(session_id_str)
    amount = checkout_session["amount_total"] / 100
    print(create_payment(checkout_session["payment_intent"],session_id_str,amount,CPID_str,PID_str,checkout_session["payment_status"]))

def retrieverefundfromStripe(intent_id):
    # Retrieve the Checkout Session
    IntentID = intent_id["intent_id"]
    intent = stripe.PaymentIntent.retrieve(IntentID)
    print(intent)
    total_amount = intent["amount"]/100
    status = intent["status"]
    URL = PAYMENTLOG_URL + IntentID
    result = invoke_http(URL, method='GET')
    CPID = result["data"]["CPID"]
    PID = result["data"]["PID"]
    session_id = result["data"]["sessionID"]
    print(result)
    print(create_payment(IntentID,session_id,total_amount,CPID,PID,status)) 

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

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receivePaymentLog()