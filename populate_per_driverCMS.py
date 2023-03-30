from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route("/get_results")
def get