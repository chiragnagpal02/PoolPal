# This is the orchestrator which will call all the endpoints and get the work done. 

from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from datetime import datetime, timedelta
from geopy.distance import geodesic
from flask_cors import CORS
from os import environ


app = Flask(__name__)

CORS(app)


THRESHOLD_DISTANC_KMS = 2

CARPOOLS_URL = 'http://127.0.0.1:5002/api/v1/carpool/get_all_carpools'
CARPEOPLE_URL = 'http://127.0.0.1:5010/api/v1/carpeople/get_all_passengers'
DRIVER_URL = 'http://127.0.0.1:5000/api/v1/driver/get_driver_by_id/'

# Passenger chooses date, start location and end location
# Have to check for 3 factors -> start location,  and date

def give_carpools_with_PID(PID):
    CPIDs = []
    all_carpools = requests.get(CARPEOPLE_URL).json()
    for i in all_carpools:
        if i['PID'] == PID:
            CPIDs.append(i['CPID'])
    return CPIDs


def get_all_existing_carpools(start_lat, start_lng, end_lat, end_lng, formatted_date, start_time_str, PID):
    response = requests.get(CARPOOLS_URL)
    statuses = {}
    passenger_start_coords = (start_lat, start_lng)
    passenger_end_coords = (end_lat, end_lng)
    passenger_start_time = datetime.strptime(start_time_str, "%H:%M:%S").time()
    # print(passenger_start_time)

    carpools = response.json()['data']['carpools']

    non_showable_carpools = give_carpools_with_PID(PID)

    final_carpools = []

    for i in carpools:
        # Convert carpool date string to datetime object
        # print()
        # print(i)
        # print()

        if i['CPID'] in non_showable_carpools:
            continue

        date = i['DateTime']
        capacity = i['Capacity_remaining']

        datetime_obj = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
        to_compare_date = datetime_obj.date()

        # Get carpool start time as datetime.time object
        start_time = datetime_obj.time()

        # Calculate lower and upper bounds of time window
        lower_time = (datetime.combine(formatted_date, passenger_start_time) - timedelta(hours=2)).time()
        upper_time = (datetime.combine(formatted_date, passenger_start_time) + timedelta(hours=2)).time()
        
        cpid = i['CPID']

        start_coords = (i['CPStartLatitude'], i['CPStartLongitude'])
        end_coords = (i['CPEndLatitude'], i['CPEndLongitude'])

        start_distance = match_carpools(start_coords, passenger_start_coords)
        end_distance = match_carpools(end_coords, passenger_end_coords)

        print(start_distance, end_distance)

        # print(f"CARPOOL DATE - {to_compare_date}")
        # print(f"PASSENGER DATE - {formatted_date}")
        # print((to_compare_date == formatted_date))

        # Check if carpool start and end locations are within 1 km of passenger locations,
        # carpool date is the same as passenger date, and carpool start time is within 2 hours
        # of passenger start time

        if (start_distance < THRESHOLD_DISTANC_KMS) and \
           (end_distance < THRESHOLD_DISTANC_KMS) and \
           (to_compare_date == formatted_date) and \
           (start_time >= lower_time) and \
           (start_time <= upper_time) and \
           (capacity > 0):
            
            print(i)
            final_carpools.append(i)
            
        

    return final_carpools

        
def match_carpools(start_coords, end_coords):
    distance = geodesic(start_coords, end_coords).km
    return distance


@app.route('/api/v1/matching/get_matching_carpools/', methods=['POST'])
def get_matching_carpools():

    start_lat = request.json.get('start_lat')
    start_lng = request.json.get('start_lng')
    end_lat = request.json.get('end_lat')
    end_lng = request.json.get('end_lng')
    time = request.json.get('time')
    date = request.json.get('date')
    PID = request.json.get('PID')
    print(start_lat, start_lng, end_lat, end_lng, time, date, PID)

    if start_lat is None or start_lng is None or end_lat is None or end_lng is None:
        return jsonify(
            {
                "error": "Missing required fields"
            }
        )

    
    # print(date)

    formatted_date = datetime.strptime(date, "%Y-%m-%d")

    date_final = formatted_date.date()

    # print(time)

    carpools = get_all_existing_carpools(float(start_lat), float(start_lng), float(end_lat), float(end_lng), date_final, time, PID)

    print()
    print(carpools)
    print()

    if len(carpools) == 0:
        return jsonify(
            {
                "error": "No matching carpools found"
            }
        )
    print(carpools)

    for carpool in carpools:
       
        DID = carpool['DID']
        # print(DID)
        url = DRIVER_URL + str(DID)
        driver_details = requests.get(url).json()['data']['driver']
        carpool['driver'] = driver_details

    

    return jsonify(
        {
            "carpools": carpools
        }
    )
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5100)

















