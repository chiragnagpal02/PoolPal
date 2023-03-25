from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import validators
from datetime import datetime


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/PoolPal'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Driver(db.Model):
    __tablename__ = 'driver'
    
    DID = db.Column(db.Integer, autoincrement=True)
    DName = db.Column(db.String(64), nullable=False)
    DGender = db.Column(db.String(1), nullable=False)
    DEmail = db.Column(db.String(64), nullable=False)
    DVehicleNo = db.Column(db.String(64), nullable=False)
    DLicenseNo = db.Column(db.String(64), nullable=False)
    DLicenseExpiration = db.Column(db.DateTime, nullable=True)
    DPhoneNo = db.Column(db.Integer, nullable=False)
    DCar = db.Column(db.String(100), nullable=False)
    DCapacity = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('DID', 'DEmail'),
        {},
    )

    def __init__(self, DName, DGender, DEmail, DVehicleNo, DLicenseNo, DLicenseExpiration, DPhoneNo, DCar, DCapacity):
        self.DName = DName
        self.DGender = DGender
        self.DEmail = DEmail
        self.DVehicleNo = DVehicleNo
        self.DLicenseNo = DLicenseNo
        self.DLicenseExpiration = DLicenseExpiration
        self.DPhoneNo = DPhoneNo
        self.DCar = DCar
        self.DCapacity = DCapacity

    def json(self):
        return {
            "DID": self.DID,
            "DName": self.DName,
            "DGender": self.DGender,
            "DEmail": self.DEmail,
            "DVehicleNo": self.DVehicleNo,
            "DLicenseNo": self.DLicenseNo,
            "DLicenseExpiration": self.DLicenseExpiration,
            "DPhoneNo": self.DPhoneNo,
            "DCar": self.DCar,
            "DCapacity": self.DCapacity
        }
    
@app.route("/", methods=['GET'])
def home():
    return render_template("templates/driver/driverSignUp.html")
    
@app.route('/api/v1/driver/get_all_drivers')

def get_all_drivers(): 
    drivers = Driver.query.all()

    if len(drivers):
        total_drivers = len(drivers)
        drivers_list = []

        for driver in drivers:
            driver_dict = driver.__dict__.copy()
            driver_dict.pop('_sa_instance_state')
            drivers_list.append(driver_dict)

        return jsonify(
            {
                "code": 200,
                "total_drivers": total_drivers,
                "data": {
                    "drivers": drivers_list
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drivers in the database."
        }
    ), 404



@app.route('/driver/get_driver_by_id/<driver_id>')
def get_driver_by_id(driver_id):
    driver = Driver.query.filter_by(DID=driver_id).first()

    if driver is not None:
        driver_dict = driver.__dict__.copy()
        driver_dict.pop('_sa_instance_state')

        return jsonify(
            {
                "code": 200,
                "data": {
                    "driver": driver_dict
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": f"There are no drivers with driver ID {driver_id}."
        }
    ), 404

@app.route('/driver/get_driver_by_licence/<license>', methods=['GET'])
def get_driver_by_licence(licence):
    driver = Driver.query.filter_by(DLicenseNo=licence).first()
    if driver:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "driver": driver.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drivers."
        }
    ), 404

@app.route("/driver/get_driver_by_email/<email>")
def get_driver_by_email(email):
    driver = Driver.query.filter_by(DEmail=email).first()
    if driver:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "driver": driver.json()
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message":f"There are no drivers with email id {email}."
        }
    ), 404


@app.route('/driver/add_driver', methods=['POST'])
def add_driver():

    DName = request.json['DName']
    DGender = request.json['DGender']
    DEmail = request.json['DEmail']
    DVehicleNo = request.json['DVehicleNo']
    DLicenseNo = request.json['DLicenseNo']
    DPhoneNo = request.json['DPhoneNo']
    DLicenseExpiration = request.json['DLicenseExpiration']
    DLicenseExpiration_Updated = datetime.strptime(DLicenseExpiration, '%Y-%m-%d')
    DCar = request.json['DCar']
    DCapacity = request.json['DCapacity']
    print(DName, DGender, DEmail, DVehicleNo, DLicenseNo, DPhoneNo, DLicenseExpiration, DCar, DCapacity)

    if not(validators.email(DEmail)):
        return jsonify(
            {
                "code": 400,
                "message": "Invalid email."
            }
        )
    
    
    driver = Driver(
        DName=DName,
        DGender=DGender, 
        DEmail=DEmail, 
        DVehicleNo=DVehicleNo, 
        DLicenseNo=DLicenseNo,
        DPhoneNo=DPhoneNo,
        DLicenseExpiration=DLicenseExpiration_Updated, 
        DCar=DCar,
        DCapacity=DCapacity
    )

    db.session.add(driver)
    db.session.commit()

    return jsonify(
        {
            "code": 200,
            "data": {
                'status': f"Driver with id {driver.DID} and {driver.DEmail} has been added successfully."
            }
        }
    )  


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
        



    

