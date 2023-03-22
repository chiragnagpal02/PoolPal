# This is the orchestrator which will call all the endpoints and get the work done. 

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DRIVER_URL = "http://127.0.0.1:5000/driver"











