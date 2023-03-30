from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

CARPEOPLE_API_URL = "http://127.0.0.1:5010/api/v1/carpeople/"
CARPOOL_API_URL = "http://127.0.0.1:5002/api/v1/carpool/"
PASSENGER_API_URL = "http://127.0.0.1:5001/api/v1/passenger/"

def get_carpools_by_driver(DID):
    url = f"{CARPOOL_API_URL}/get_carpool_by_driver_id/{DID}"
    response = requests.get(url)
    carpools = response.json()['data']['carpools']
    return carpools

def get_passengers_for_carpool(carpools):
    for carpool in carpools:
        CPID = carpool['CPID']
        url = f"{CARPEOPLE_API_URL}/get_passengers/{CPID}"
        response = requests.get(url)
        passengers = response.json()

        for passenger in passengers:
            PID = passenger['PID']
            print(PID)
            passenger['name'] = get_passenger_name(passenger['PID'])
            print(passenger['name'])

        carpool['passengers'] = passengers
    return carpools

def get_passenger_name(PID):
    url = f"{PASSENGER_API_URL}/get_passenger_by_id/{PID}"
    print(url)
    content = requests.get(url)
    pname = content.json()['data']['passenger']['PName']
    return pname

@app.route("/get_carpools_with_passengers/<int:DID>")
def get_carpools_with_passengers(DID):
    carpools = get_carpools_by_driver(DID)
    print(len(carpools))
    final_return_carpools = get_passengers_for_carpool(carpools)
    # print(result)
    return final_return_carpools

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5700)