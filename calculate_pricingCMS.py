# call fuel api, get the distance between the 2 pairs of coordinates and caluculate the base price for the 
# journey. Return the base price. 

from geopy.distance import geodesic
from flask import Flask, request, jsonify

app = Flask(__name__)

AVERAGE_SINGAPORE_FUEL_PRICES = 2.6 # per liter price
AVERAGE_MILEAGE_SINGAPORE_CARS = 16 # kmpl

def calculate_price(start_lat, start_long, end_lat, end_long):
    distance = calculate_distance(start_lat, start_long, end_lat, end_long)

    unit_distance_travelled = distance / AVERAGE_MILEAGE_SINGAPORE_CARS
    return AVERAGE_SINGAPORE_FUEL_PRICES * unit_distance_travelled

def calculate_distance(start_lat, start_long, end_lat, end_long):
    starting_coordinates = (start_lat, start_long)
    ending_coordinates = (end_lat, end_long)

    return geodesic(starting_coordinates, ending_coordinates).km


@app.route("/api/v1/base_price/<start_lat>,<start_long>/<end_lat>,<end_long>", methods=['GET'])
def get_base_price(start_lat, start_long, end_lat, end_long):
    base_price = calculate_price(start_lat, start_long, end_lat, end_long)
    return base_price

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5101)