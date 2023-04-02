from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

# PAYMENT_LOGS_API = "http://127.0.0.1:5015/api/v1/paymentlog/get_intent_by_CPID_PID/<int:CPID>/<int:PID>"
PAYMENT_LOGS_API = "http://127.0.0.1:5055/api/v1/paymentlog/get_intent_by_ID"
# PAYMENTS_API_BASE_URL = 'http://127.0.0.1:5004/api/v1/payments/refund/<intentID>/<int:refundAmount>'
PAYMENTS_API_BASE_URL = 'http://127.0.0.1:5004/api/v1/payments/refund'

@app.route('/api/v1/process_refund/<float:refundedAmount>/<int:CPID>/<int:PID>')
def process_refund(refundedAmount, CPID, PID):

    intentID = get_intentID(CPID,PID)

    refund_status = process_refund(intentID, refundedAmount)

    return refund_status

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
    status = response.json()
    print(f"Get refund Status : {status}")

    try:
        return status
    
    except Exception as e:
        print(f"Failed to decode JSON response: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5120)