from flask import Flask, request, jsonify
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import bcrypt
import amqp_setup
import pika
import json
import validators

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

app.app_context().push()

db = SQLAlchemy(app)
CORS(app)


class Staff(db.Model):
    __tablename__ = 'staff'

    SID = db.Column(db.Integer, primary_key=True, nullable=False)
    SName = db.Column(db.String(100), nullable=False)
    SEmail = db.Column(db.String(1), nullable=False)
    SPasswordHash = db.Column(db.String(100), nullable=False)

    def __init__(self, SName,SEmail,SPasswordHash):
        #self.SID = SID
        self.SName = SName
        self.SEmail = SEmail
        self.SPasswordHash = SPasswordHash

    def json(self):
        return {"SID": self.SID, "SName": self.SName, "SEmail" : self.SEmail, "SPasswordHash" : self.SPasswordHash}


@app.route("/api/v1/staff/get_all_staff")
def get_all():
    stafflist = Staff.query.all()
    if len(stafflist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff": [staff.json() for staff in stafflist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no staff."
        }
    ), 404

@app.route("/api/v1/staff/get_staff_by_staffid/<int:SID>")
def find_by_sid(SID):
    staff = Staff.query.filter_by(SID=SID).first()
    if staff:
        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404

@app.route("/api/v1/staff/create_staff/", methods=['POST'])
def create_staff():
    #data = request.get_json()
    salt = bcrypt.gensalt()
    SName = request.json.get('SName')
    SEmail = request.json.get('SEmail')
    SPassword = request.json.get('SPassword')
    SPasswordHash = bcrypt.hashpw(SPassword.encode('utf-8'), salt)
    staff = Staff(SName,SEmail,SPasswordHash)

    # Check if a staff with the same email address already exists
    existing_staff = Staff.query.filter_by(SEmail=SEmail).first()
    if existing_staff:
        return jsonify({
            "code": 400,
            "message": "A staff with this email address already exists."
        }), 400

    # Validate email address
    if not validators.email(SEmail):
        return jsonify({
            "code": 400,
            "message": "Invalid email.",
            "email": f"{SEmail} is not a valid email."
        }), 400
    
    try:
        db.session.add(staff)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the staff."
            }
        ), 500

    add_user = {
        "Email" : staff.SEmail,
        "Role" : "Staff"
    }

    processAddUser(add_user)

    return jsonify(
        {
            "code": 201,
            "data": staff.json()
        }
    ), 201


@app.route("/api/v1/staff/update_staff/<int:SID>", methods=['PUT'])
def update_staff(SID):
    try:
        staff = Staff.query.filter_by(SID=SID).first()
        if not staff:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "SID": SID
                    },
                    "message": "Staff not found."
                }
            ), 404

         # update multiple columns
        data = request.get_json()
        if 'SName' in data:
            staff.SName = data['SName']

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "SID": SID
                },
                "message": "An error occurred while updating the staff details. " + str(e)
            }
        ), 500

def processAddUser(user):
    print('\n-----Invoking user microservice-----')
    message = json.dumps(user)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="create.user", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    
    return {
        "code": 201,
        "data": {
            "user_result": user
        }
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5007)
