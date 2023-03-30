from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import amqp_setup
import pika
import json

from invokes import invoke_http

import json
import os

import amqp_setup

monitorBindingKey='*.payment'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)

class PaymentLogs(db.Model):
    __tablename__ = 'paymentlog'
    
    ID = db.Column(db.Integer, autoincrement=True)
    LogContent = db.Column(db.String(1000), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('ID'),
        {},
    )

    def __init__(self, ID, LogContent):
        self.ID = ID
        self.LogContent = LogContent

    def json(self):
        return {
            "ID": self.ID,
            "LogContent": self.LogContent,
        }

def receiveOrderLog():
    amqp_setup.check_setup()
        
    queue_name = 'Payment_Log'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an payment log by " + __file__)
    processOrderLog(json.loads(body))
    print() # print a new line feed

def processOrderLog(order):
    print("Recording an payment log:")
    print(order)
    print(create_payment(order))

@app.route("/api/v1/paymentlogs", methods=['POST'])
def create_payment(data):
    #data = request.get_json()
    print(data)
    logs = PaymentLogs('', str(data))

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
    receiveOrderLog()