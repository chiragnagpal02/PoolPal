from flask import Blueprint, request, jsonify, render_template
from src.databases import Driver, db


driver = Blueprint('driver', __name__, url_prefix='/api/driver')


@driver.route('/get_all_drivers')
def get_all_drivers(): 
    drivers = Driver.query.all()
    if len(drivers):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "drivers": [driver.json() for driver in drivers]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no drivers."
        }
    ), 404


@driver.route('/get_driver_by_id/<driver_id>')
def get_driver_by_id(driver_id):
    driver = Driver.query.filter_by(DID=driver_id).first()
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

@driver.route('/get_driver_by_licence/<license>', methods=['GET'])
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


@driver.route('/add_driver', methods=['POST'])
def add_driver():
    DName = request.json['DName']
    DGender = request.json['DGender']
    DEmail = request.json['DEmail']
    DVehicleNo = request.json['DVehicleNo']
    DLicenseNo = request.json['DLicenseNo']
    DPhoneNo = request.json['DPhoneNo']
    DLicenseExpiration = request.json['DLicenseExpiration']
    DCar = request.json['DCar']
    DCapacity = request.json['DCapacity']

    driver = Driver(DName, DGender, DEmail, DVehicleNo, DLicenseNo, DPhoneNo, DLicenseExpiration, DCar, DCapacity)

    db.session.add(driver)
    db.session.commit()

    return jsonify(
        {
            "code": 200,
            "data": {
                'status': f"Driver with id {driver.DID} has been added successfully."
            }
        }
    )
    
