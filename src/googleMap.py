from flask import render_template, request, Blueprint, jsonify
import requests

googleMap = Blueprint('googleMap', __name__, url_prefix='/map', template_folder='../backend/templates') 

# Set up Google Maps API keys
# search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
# details_url = "https://maps.googleapis.com/maps/api/place/details/json"
# key = 'AIzaSyAu5xYBC5OCuZImTFY1xt81NdOnhP0IB_g'

@googleMap.route("/", methods=["GET"])
def retreive():
    return render_template('test.html') 

# @googleMap.route("/sendRequest/<string:query>")
# def results(query):
# 	search_payload = {"key":key, "query":query}
# 	search_req = requests.get(search_url, params=search_payload)
# 	search_json = search_req.json()

# 	place_id = search_json["results"][0]["place_id"]

# 	details_payload = {"key":key, "placeid":place_id}
# 	details_resp = requests.get(details_url, params=details_payload)
# 	details_json = details_resp.json()

# 	url = details_json["result"]["url"]
# 	return jsonify({'result' : url})

