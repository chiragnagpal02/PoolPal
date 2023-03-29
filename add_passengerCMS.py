from flask import Flask, request, jsonify
import requests

# step 1 - Get the carpool details from the carpool API to check the capacity remaining
# step 2 - If the capacity is greater than 0, then subtract 1 from the capacity_remaining else return the error message
# step 3 - if not, call the carpeople ms to add the passenger to the carpool
app = Flask(__name__)

# Adding the passenger in a particular carpool using the carpeople MS

def add_person(CPID, DID, PID, PEmail):
    url = 'http://127.0.0.1:5010/api/v1/carpeople/add_passenger/' + str(CPID) + '/' + str(DID) + '/' + str(PID) + '/' + str(PEmail)
    response = requests.get(url)
    return response.json()

# def get_passengers_in_carpool(CPID):
#     url = 'http://127.0.0.1:5010/api/v1/carpeople/get_passengers/' + str(CPID)
#     passengers = requests.get(url)
#     number_of_registered_passengers = len(passengers)
#     return passengers, number_of_registered_passengers

def carpool_remaining_capacity(CPID):
    url = 'http://127.0.0.1:5010/api/v1/carpool/get_carpool_by_id/' + str(CPID)
    response = requests.get(url)
    carpool_capacity = response['data']['carpool']['Capacity_remaining']
    return carpool_capacity

def update_passenger_price_of_carpool(CPID):
    carpool_details = 
    url = 'http://127.0.0.1:5010/api/v1/carpool/update_passenger_price/' + str(CPID)
    response = requests.get(url)
    return response.json()
    
def update_capacity_in_carpool_table(CPID):
    url = 'http://127.0.0.1:5010//api/v1/carpool/update_carpool_capacity/' + str(CPID)
    response = requests.get(url)
    response_status = response.status_code
    if response_status == 400:
        return False
    
    return response.json()

@app.route('/add_passenger/<CPID>,<DID>,<PID>,<PEmail>', methods=['POST'])
def add_passenger():
