from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

PAYMENT_LOGS_API = "http://127.0.0.1:5010/api/v1/paymentlogs"
PAYMENTS_API_BASE_URL = 'http://127.0.0.1:5004/api/v1/payments/refund/<int:intentID>/<int:refundAmount>'

@app.route('/process_refund/<int:refundAmount>/<int:CPID>/<int:PID>')
def process_refund(refundedAmount, CPID):
    return ""
    # return redirect(f"{PAYMENTS_API_BASE_URL}/{intentID}/{refundedAmount")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5120)
