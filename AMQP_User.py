from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import amqp_setup
import pika
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)

monitorBindingKey='*.user'

class User(db.Model):
    __tablename__ = 'user'

    Email = db.Column(db.String(100), primary_key=True, nullable=False)
    Role = db.Column(db.String(100), nullable=False)

    def __init__(self, Email, Role):
        self.Email = Email
        self.Role = Role

    def json(self):
        return {"Email": self.Email, "Role": self.Role}

def receiveUserLog():
    amqp_setup.check_setup()
        
    queue_name = 'User'
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived a user by " + __file__)
    routing_key = method.routing_key
    print("Received a message with routing key:", routing_key)
    processUserLog(json.loads(body),routing_key)
    print() # print a new line feed

def processUserLog(user,routing_key):
    print("Recording an user log:")
    print(user)
    if (routing_key == "create.user") :
        print(create_user(user["Email"],user["Role"]))
    else :
        print(find_by_email(user))

@app.route("/user")
def get_all():
    userlist = User.query.all()
    if len(userlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "user": [user.json() for user in userlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no user."
        }
    ), 404


@app.route("/create_user", methods=['POST'])
def create_user(Email, role):
    if (User.query.filter_by(Email=Email).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "Email": Email
                },
                "message": "User already exists."
            }
        ), 400
    
    user = User(Email, role)

    try:
        db.session.add(user)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Email": Email
                },
                "message": "An error occurred creating the user."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": user.json()
        }
    ), 201


@app.route("/update_user", methods=['PUT'])
def update_user(Email,Role):
    try:
        user = User.query.filter_by(Email=Email).first()
        if not user:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "Email": Email
                    },
                    "message": "user not found."
                }
            ), 404

        # update multiple columns
        #data = request.get_json()
        if (Email != ""):
            user.Email = Email
        if (Role != ""):
            user.Role = Role

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Email": Email
                },
                "message": "An error occurred while updating the user. " + str(e)
            }
        ), 500

@app.route("/api/v1/user/get_user_by_email/<string:Email>")
def find_by_email(user):
    Email = user["Email"]
    print(Email)
    user = User.query.filter_by(Email=Email).first()
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404

if __name__ == '__main__':
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveUserLog()