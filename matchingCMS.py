# This is the orchestrator which will call all the endpoints and get the work done. 

from flask import Flask, request, jsonify
import requests
from geopy.distance import geodesic

app = Flask(__name__)

THRESHOLD_DISTANCE = 2
CARPOOLS_URL = 'http://127.0.0.1:5002/get_all_carpools'

# Passenger chooses date, start location and end location

def get_all_existing_carpools(start_lat, start_lng):
    response = requests.get(CARPOOLS_URL)
    statuses = {}
    passenger_coords = (start_lat, start_lng)
    carpools = response.json()['data']['carpools']
    for i in carpools:
        cpid = i['CPID']
        start_location = i['CPStartLocation']

        start_coords = (i['CPStartLatitude'], i['CPStartLongitude'])
        
        # print(start_coords)
        # print(end_coords)
       
        distance = match_carpools(start_coords, passenger_coords)
        print(f"{cpid}: Distance between {start_location} and Passenger Coordinates is {round(distance, 2)} kms!")
        
        # check for the threshold distance

        if distance < THRESHOLD_DISTANCE:
            statuses[cpid] = True
        else:
            statuses[cpid] = False
    
    return carpools, statuses
        

def match_carpools(start_coords, end_coords):
    distance = geodesic(start_coords, end_coords).km
    return distance

def send_matching_carpools(start_lat, start_lng):
    carpools, statuses = get_all_existing_carpools(start_lat, start_lng)
    final_carpools = []
    for i in carpools:
        cpid = i['CPID']
        status = statuses[cpid]

        if status:
            final_carpools.append(i)
    
    return final_carpools 

@app.route('/get_matching_carpools/<float:start_lat>,<float:start_lng>/', methods=['GET'])
def get_matching_carpools(start_lat, start_lng):
    carpools = send_matching_carpools(start_lat, start_lng)
    print(carpools)
    return jsonify(carpools)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5100)

















