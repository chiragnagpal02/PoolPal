from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import os, sys
import requests
from geopy.distance import geodesic


app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

CARPOOL_API_BASE_URL = environ.get('carpool_URL') or 'http://127.0.0.1:5002/api/v1/carpool'


def get_carpool_distance(CPID):
    # payload = {
    #     'CPID': CPID
    #     }
    url = f'{CARPOOL_API_BASE_URL}/get_carpool_by_id/{CPID}'
    response = requests.get(url)
    start_lat = response.json()['data']['carpool']['CPStartLatitude']
    start_long = response.json()['data']['carpool']['CPStartLongitude']
    end_lat = response.json()['data']['carpool']['CPEndLatitude']
    end_long = response.json()['data']['carpool']['CPEndLongitude']

    carpool_distance = calculate_distance(start_lat, start_long, end_lat, end_long)

    print(f"Get Carpool distance : {carpool_distance}")

    try:
        return carpool_distance
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None
    
def get_travelled_distance(CPID, end_lat, end_long):
    # payload = {
    #     'CPID': CPID
    #     }
    url = f'{CARPOOL_API_BASE_URL}/get_carpool_by_id/{CPID}'
    response = requests.get(url)
    start_lat = response.json()['data']['carpool']['CPStartLatitude']
    start_long = response.json()['data']['carpool']['CPStartLongitude']

    travelled_distance = calculate_distance(start_lat, start_long, end_lat, end_long)

    print(f"Get Travelled distance : {travelled_distance}")

    try:
        return travelled_distance
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None
    
def get_passenger_price(CPID):
    # payload = {
    #     'CPID': CPID
    #     }
    url = f'{CARPOOL_API_BASE_URL}/get_carpool_by_id/{CPID}'
    response = requests.get(url)
    passenger_price = response.json()['data']['carpool']['PassengerPrice']
    print(f"Get Passenger Price : {passenger_price}")

    try:
        return passenger_price
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None
    
def calculate_distance(start_lat, start_long, end_lat, end_long):
    starting_coordinates = (start_lat, start_long)
    ending_coordinates = (end_lat, end_long)

    return geodesic(starting_coordinates, ending_coordinates).km


@app.route('/api/v1/calculate_refund_amount/<int:CPID>/<end_lat>,<end_long>', methods=['GET'])
def calculate_refund_amount(CPID, end_lat, end_long):

    # refunded_process_status = False
    
    # Calculates travelled distance
    travelled_distance = get_travelled_distance(CPID, end_lat, end_long)
    # Get carpool distance
    carpool_distance = get_carpool_distance(CPID)
    # Get carpool price
    passenger_price = int(get_passenger_price(CPID))

    refunded_price = (travelled_distance/carpool_distance) * passenger_price

    return jsonify({
        'price': round(refunded_price)
        # 'status': refunded_process_status
    })

    # url = f"{PROCESS_REFUND_API_URL}/{refunded_price}/{CPID}/{PID}"

    # response = requests.get(url)

    # if response.status_code == 200:
    # # process the response data
    #     refunded_process_status = True
    # else:
    #     # handle the error
    #     print('Error:', response.status_code)


    # call here to that process CMS and then get a status as a reponse - 
    # {"Status": "Success"} or {"Status": "Failed"}
    # if status == "Success":
    #     return jsonify({
    #             "price": refunded_price

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5115)

