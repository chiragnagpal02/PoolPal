# This is the orchestrator which will call all the endpoints and get the work done. 

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# Passenger chooses date, start location and end location


def get_all_existing_carpools():
    url = 'http://127.0.0.1:5002/get_all_carpools'
    response = requests.get(url)
    for i in response.json()['data']['carpools']:
        print(i)
        print()

def match_carpools():
    pass


get_all_existing_carpools()
















