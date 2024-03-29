from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

import requests



app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

PAYMENT_LOGS_API = environ.get('paymentlog_URL') or "http://127.0.0.1:5055/api/v1/paymentlog/get_intent_by_ID"
PAYMENTS_API_BASE_URL = environ.get('payment_URL') or 'http://127.0.0.1:5004/api/v1/payments/refund'

@app.route('/api/v1/process_refund/<int:refundedAmount>/<int:CPID>/<int:PID>')
def process_refund(refundedAmount, CPID, PID):

    intentID = get_intentID(CPID,PID)

    refund_status = process_refund(intentID, refundedAmount)

    return jsonify({
        'price': refundedAmount,
        'status': refund_status,
    })

def get_intentID(CPID,PID):

    url = f'{PAYMENT_LOGS_API}/{CPID}/{PID}'
    response = requests.get(url)
    
    intentID = response.json()['data']["intentID"]
    print(f"Get Intent ID : {intentID}")

    try:
        return intentID
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None
    
def process_refund(intentID, refundedAmount):

    url= f"{PAYMENTS_API_BASE_URL}/{intentID}/{refundedAmount}"
    response = requests.get(url)
    print(response.json())
    # print(f"Get refund Status : {response.json()}")

    try:
        return response.json()
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5120)