from flask import Blueprint, jsonify, request
from src.database import Drivers, db
from constants.http_status_codes import *



drivers = Blueprint('drivers', __name__, url_prefix='/api/v1/drivers')


@drivers.route('/create', methods=['POST'])
def create_driver():
    dname = request.json['DName']
    dage = request.json['DAge']
    dgender = request.json['DGender']
    demail = request.json['DEmail']
    daddress = request.json['DAddress']
    dvehicle = request.json['DVehicleNo']
    dlicense = request.json['DLicenseNo']
    dphone = request.json['DPhone']
    

    new_driver = Drivers(
        DName=dname,
        DAge=dage,
        DGender=dgender,
        DEmail=demail,
        DAddress=daddress,
        DVehicleNo=dvehicle,
        DLicenseNo=dlicense,
        DPhone=dphone,
        
    )

    db.session.add(new_driver)
    db.session.commit()
    
    return jsonify({
        "message": "Driver created successfully",
        'driver': {
            'Driver Name': new_driver.DName,
            'Driver Age': new_driver.DAge,
            'Driver Gender': new_driver.DGender,
            'Driver Email': new_driver.DEmail,
            'Driver Address': new_driver.DAddress,
            'Driver Vehicle No': new_driver.DVehicleNo,
            'Driver License No': new_driver.DLicenseNo,
            'Driver Phone': new_driver.DPhone,
            }
        }), HTTP_201_CREATED


@drivers.route('/me')
def me():
    return {'message': 'User Me'}
