from flask import Flask, request, jsonify, redirect
import requests
from geopy.distance import geodesic

app = Flask(__name__)

CARPOOL_API_BASE_URL = 'http://127.0.0.1:5002/api/v1/carpool/'
PROCESS_REFUND_API_URL = 'http://127.0.0.1:5120/process_refund/<int:refundAmount>/<int:CPID>/<int:PID>'

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


@app.route('/api/v1/calculate_refund_amount/<int:CPID>/<int:PID>/<end_lat>,<end_long>', methods=['GET'])
def calculate_refund_amount(CPID, PID, end_lat, end_long):
    
    # Calculates travelled distance
    travelled_distance = get_travelled_distance(CPID, end_lat, end_long)
    # Get carpool distance
    carpool_distance = get_carpool_distance(CPID)
    # Get carpool price
    passenger_price = int(get_passenger_price(CPID))

    refunded_price = (travelled_distance/carpool_distance) * passenger_price

    process_refund_status = f"{PROCESS_REFUND_API_URL}/{refunded_price}/{CPID}/{PID}"

    # call here to that process CMS and then get a status as a reponse - 
    # {"Status": "Success"} or {"Status": "Failed"}
    # if status == "Success":
    #     return jsonify({
    #             "price": refunded_price

    return jsonify({
        'price': refunded_price,
        'status': process_refund_status
    })


# calculate the price + initiate refund from stripe payment

# takes in the CPID + coordinates of where the person gets off -> calls the carpool MS for the total coordinates



'''
get <start_lat>,<start_long>/<end_lat>,<end_long> from carpool MS by inputting MS

this for total distance of carpool 
@app.route("/api/v1/calculate_price_between_points/<start_lat>,<start_long>/<end_lat>,<end_long>", methods=['GET'])
def get_price_between_points(start_lat, start_long, end_lat, end_long):
    return a = calculate_distance(start_lat, start_long, end_lat, end_long)

this is travelled distance before refund
@app.route("/api/v1/calculate_price_between_points/<start_lat>,<start_long>/<end_lat_of_pass>,<end_long_of_pass>", methods=['GET'])
def get_price_between_points(start_lat, start_long, end_lat, end_long):
    return b = calculate_distance(start_lat, start_long, end_lat, end_long)

also need to get passenger_price from carpool MS 

refunded_price = (b/a)*passenger_price

return refunded_price

# SEPERATE MS - 
call the refund payments once in payments MS and give intent ID + amount which you get from here. 
'''

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5115)

