from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DRIVER_URL = 'http://127.0.0.1:5000/api/v1/driver/get_all_drivers'
PASSENGER_URL = 'http://127.0.0.1:5001/api/v1/get_all_passengers'
STAFF_URL = 'http://127.0.0.1:5007/staff'

def get_existing_driverDetails():
    response = requests.get(DRIVER_URL)
    driverID = response.json()['data']['Driver']
    for i in driverID:
        dID = i['DID']
        dName = i['DName']
        dVeh = i['DVehicleNo']
        dNo = i['DPhoneNo'] 


def get_existing_PassengerDetails():
    response = requests.get(PASSENGER_URL)
    passengerID = response.json()['data']['Passengers']
    for i in passengerID:
        pID = i['PID']
        pName = i['PName']
        dNo = i['PPhone'] 

def staffDetails():
    response = requests.get(PASSENGER_URL)
    staffID = response.json()['data']['Staff']
    for i in staffID:
        sID = i['SID']
        sName = i['SName']

