from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CARPOOL_API_BASE_URL = 'http://127.0.0.1:5002'
CARPEOPLE_API_BASE_URL = 'http://127.0.0.1:5010'

def add_passenger_to_carpeople(CPID, DID, PID, PEmail):
    payload = {
        'CPID': CPID,
        'DID': DID,
        'PID': PID,
        'PEmail': PEmail
        }
    url = f'{CARPEOPLE_API_BASE_URL}/api/v1/carpeople/add_passenger'
    response = requests.post(url, json=payload)
    print(f"Add Passenger to Carpeople : {response}")
    try:
        return response.json()
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None

def get_passengers_in_carpool(CPID):
    url = f'{CARPEOPLE_API_BASE_URL}/api/v1/carpeople/get_passengers/{CPID}'
    response = requests.get(url)
    print(f"get passengers in carpool : {response}")
    if response.status_code == 200:
        passengers = response.json()
        number_of_registered_passengers = len(passengers)
        return passengers, number_of_registered_passengers
    else:
        return None, 0

def get_carpool_by_id(CPID):
    url = f'{CARPOOL_API_BASE_URL}/api/v1/carpool/get_carpool_by_id/{CPID}'
    response = requests.get(url)
    print(f"Add carpool by id : {response}")
    if response.status_code == 200:

        carpool_capacity_remaining = response.json()['data']['carpool']['Capacity_remaining']
        carpool_price = response.json()['data']['carpool']['CarpoolPrice']

        return carpool_capacity_remaining, carpool_price
    else:
        return None

def update_passenger_price_of_carpool(CPID, passenger_price):
    url = f'{CARPOOL_API_BASE_URL}/api/v1/carpool/update_passenger_price/{CPID}'
    payload = {'PassengerPrice': passenger_price}
    response = requests.put(url, json=payload)
    print(url)
    return response.json()

def update_capacity_in_carpool_table(CPID):
    url = f'{CARPOOL_API_BASE_URL}/api/v1/carpool/update_carpool_capacity/{CPID}'
    response = requests.put(url)
    print(response)
    if response.status_code == 200:
        return True
    else:
        return False

@app.route('/add_passenger/<int:CPID>/<int:DID>/<int:PID>/<PEmail>', methods=['GET'])
def add_passenger(CPID, DID, PID, PEmail):
    carpool_capacity, carpool_price = get_carpool_by_id(CPID)

    if carpool_capacity > 0:
        # Update the capacity of the carpool in the carpool table
        updated_capacity = update_capacity_in_carpool_table(CPID)

        # Add the passenger to the carpeople table
        added_passenger = add_passenger_to_carpeople(CPID, DID, PID, PEmail)

        # Get the list of registered passengers for the updated carpool
        registered_passengers, num_registered_passengers = get_passengers_in_carpool(CPID)

        # If this is the first passenger, update the carpool price to the passenger price
        if num_registered_passengers == 1:

            total_people_in_car = num_registered_passengers + 1
            new_passenger_price = round(carpool_price/total_people_in_car, 2)

            update_passenger_price_of_carpool(CPID, new_passenger_price)

        # Return a response with details about the updated carpool and passenger
        response_data = {
            'carpool': {
                'id': CPID,
                'updated_capacity': updated_capacity,
                'registered_passengers': registered_passengers,
                'remaining_capacity': carpool_capacity - num_registered_passengers,
                'updated_passenger_price': new_passenger_price
            },
            'passenger': {
                'id': PID,
                'added_to_carpool': CPID,
                'email': PEmail
            }
        }

        try:
            return jsonify({
                'code': 200,
                'data': response_data
            }), 200
        except ValueError:
            return jsonify({
                'code': 500,
                'message': 'Internal server error: Could not decode JSON response from carpeople service'
            }), 500
    else:
        return jsonify({
            'code': 400,
            'message': 'Carpool is already full'
        }), 400
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5110)






