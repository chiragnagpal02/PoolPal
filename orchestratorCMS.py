# This is the orchestrator which will call all the endpoints and get the work done. 

from flask import Flask, request, jsonify
import requests
from geopy.distance import geodesic

app = Flask(__name__)

THRESHOLD_DISTANCE = 1
CARPOOLS_URL = 'http://127.0.0.1:5002/get_all_carpools'
# Passenger chooses date, start location and end location


def get_all_existing_carpools():
    response = requests.get(CARPOOLS_URL)
    statuses = {}
    carpools = response.json()['data']['carpools']
    for i in carpools:
        cpid = i['CPID']
        start_location = i['CPStartLocation']
        end_location = i['CPEndLocation']

        start_coords = (i['CPStartLatitude'], i['CPStartLongitude'])
        end_coords = (i['CPEndLatitude'], i['CPEndLongitude'])
        # print(start_coords)
        # print(end_coords)
       
        distance = match_carpools(start_coords, end_coords)
        print(f"{cpid}: Distance between {start_location} and {end_location} is {round(distance, 2)} kms!")
        
        # check for the threshold distance

        if distance < THRESHOLD_DISTANCE:
            statuses[cpid] = True
        else:
            statuses[cpid] = False
    
    send_matching_carpools(carpools, statuses)
        

def match_carpools(start_coords, end_coords):
    distance = geodesic(start_coords, end_coords).km
    return distance

def send_matching_carpools(carpools, statuses):
    for i in carpools:
        cpid = i['CPID']
        if statuses[cpid]:
            print(f"{cpid} is matched!")
        else:
            print(f"{cpid} is not matched!")





get_all_existing_carpools()
















