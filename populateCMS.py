from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

CARPEOPLE_API_URL = "http://127.0.0.1:5010/api/v1/carpeople/"
CARPOOL_API_URL = "http://127.0.0.1:5002/api/v1/carpool/"
PASSENGER_API_URL = "http://127.0.0.1:5001/api/v1/passenger/"
DRIVER_API_URL = "http://127.0.0.1:5000/api/v1/driver/"

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

@app.route("/get_carpools_by_driver/<int:DID>")
def get_carpools_with_passengers(DID):
    carpools = get_carpools_by_driver(DID)
    print(len(carpools))
    final_return_carpools = get_passengers_for_carpool(carpools)
    # print(result)
    return final_return_carpools

@app.route("/get_carpools_by_passenger/<int:PID>")
def get_carpool_by_passenger(PID):
    
    url1 = f"{CARPEOPLE_API_URL}/get_all_by_PID/{PID}"
    url2 = f"{CARPOOL_API_URL}/get_all_carpools"
    url3 = f"{DRIVER_API_URL}/get_driver_by_id/"

    passengers = requests.get(url1).json()
    carpool_json = requests.get(url2)
    carpools = carpool_json.json()['data']['carpools']
    
    CPIDs = [passenger['CPID'] for passenger in passengers]
    
    all_carpools = []

    for carpool in carpools:
        if carpool['CPID'] in CPIDs:
            DID = carpool['DID']
            final_url = url3 + str(DID)
            driver = requests.get(final_url).json()['data']['driver']
            carpool['driver'] = driver
            all_carpools.append(carpool)

    return jsonify(all_carpools)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5700)