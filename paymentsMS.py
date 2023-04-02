# from flask import Flask, render_template, request, jsonify
# import stripe


# app = Flask(__name__)

# stripe_keys = {
#   'secret_key': 'sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR',
#   'publishable_key': 'pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh'
# }

# stripe.api_key = stripe_keys["secret_key"]

# @app.route('/api/v1/payments/')
# def index():
#     return render_template('index.html', key=stripe_keys['publishable_key'])

# @app.route("/api/v1/payments/success")
# def success():
#     return render_template("success.html")


# @app.route("/api/v1/payments/cancelled")
# def cancelled():
#     return render_template("cancelled.html")

# @app.route("/api/v1/payments/config")
# def get_publishable_key():
#     stripe_config = {"publicKey": "pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh"}
#     return jsonify(stripe_config)

# # @app.route("/api/v1/payments/create-payment-intent", methods=["POST"])
# # def create_payment_intent():
# #     amount = request.json["amount"]
# #     currency = "sgd"

# #     payment_intent = stripe.PaymentIntent.create(
# #         amount=amount,
# #         currency=currency
# #     )

# #     return jsonify({"client_secret": payment_intent.client_secret})

# @app.route("/api/v1/payments/create-checkout-session/", methods=["POST"])
# def create_checkout_session(amount):
#     amount = request.json["amount"]
#     # domain_url = "http://127.0.0.1:5020/api/v1/payments/"
#     stripe.api_key = "sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR"

#     try:
#         # Create new Checkout Session for the order
#         # Other optional params include:
#         # [billing_address_collection] - to display billing address details on the page
#         # [customer] - if you have an existing Stripe Customer ID
#         # [payment_intent_data] - capture the payment later
#         # [customer_email] - prefill the email input in the form
#         # For full details see https://stripe.com/docs/api/checkout/sessions/create

#         # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
#         checkout_session = stripe.checkout.Session.create(
#             line_items=[{
#                 'price_data': {
#                 'currency': 'sgd',
#                 f'unit_amount': {amount},
#                 'product_data': {
#                     'name': 'PoolPal',
#                     'description': 'Your Ride Journey',
#                     # 'images': ['https://example.com/t-shirt.png'],
#                 },
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url='http://127.0.0.1:5000/api/v1/payments/success?session_id={CHECKOUT_SESSION_ID}',
#             cancel_url='http://127.0.0.1:5000/api/v1/payments/cancelled',
#             )
#         return jsonify({"sessionId": checkout_session["id"]})
#     except Exception as e:
#         print(e)
#         return jsonify(error=str(e)), 403

# if __name__ == '__main__':
#     app.run(host= "0.0.0.0", debug=True, port=5004)

from flask import Flask, render_template, request, jsonify, redirect, url_for
import stripe
import amqp_setup
import pika
import json
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

stripe_keys = {
  'secret_key': 'sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR',
  'publishable_key': 'pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh'
}

stripe.api_key = stripe_keys["secret_key"]


@app.route('/api/v1/payments/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])


@app.route("/api/v1/payments/success")
def success():
    session_id = request.args.get("session_id")
    CPID = request.args.get("CPID")
    PID = request.args.get("PID")
    processAddPaymentLogs(session_id,CPID,PID)
    return render_template("success.html")


@app.route("/api/v1/payments/cancelled")
def cancelled():
    session_id = request.args.get("session_id")
    CPID = request.args.get("CPID")
    PID = request.args.get("PID")
    processAddPaymentLogs(session_id,CPID,PID)
    return render_template("cancelled.html")


@app.route("/api/v1/payments/config")
def get_publishable_key():
    stripe_config = {"publicKey": "pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh"}
    return jsonify(stripe_config)


@app.route("/api/v1/payments/create-checkout-session/<int:amount>/<int:CPID>/<int:PID>")
def create_checkout_session(amount,CPID,PID):
    amount_in_sgd = amount*100
    stripe.api_key = stripe_keys["secret_key"]

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - capture the payment later
        # [customer_email] - prefill the email input in the form
        # For full details see https://stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                'currency': 'sgd',
                'unit_amount': int(amount_in_sgd),
                'product_data': {
                    'name': 'PoolPal',
                    'description': 'Your Ride Journey',
                    # 'images': ['https://example.com/t-shirt.png'],
                },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:5004/api/v1/payments/success?session_id={CHECKOUT_SESSION_ID}&CPID=' + str(CPID) + '&PID=' + str(PID),
            cancel_url='http://127.0.0.1:5004/api/v1/payments/cancelled?session_id={CHECKOUT_SESSION_ID}&CPID=' + str(CPID) + '&PID=' + str(PID),
            )
        return redirect(checkout_session.url)
    except Exception as e:
        print(e)
        return jsonify(error=str(e)), 403

def processAddPaymentLogs(session_id,CPID,PID):
    print('\n-----Invoking Payment log microservice-----')
    payment_details = {
        "session_id" : session_id,
        "CPID" : CPID,
        "PID" : PID
    }
    print(payment_details)
    message = json.dumps(payment_details)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="create.payment", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
    
    return {
        "code": 201,
        "data": {
            "payment_logs_result": payment_details
        }
    }

@app.route("/api/v1/payments/refund/<intentID>/<float:refundedAmount>")
def refund(intentID, refundedAmount):
    # payment_intent_id = request.form.get('payment_intent_id')
    # amount = request.form.get('amount')
    stripe.api_key = stripe_keys["secret_key"]
    try:
        refund = stripe.Refund.create(
            payment_intent=intentID,
            amount=int(refundedAmount),
        )
        if refund.status == 'succeeded':
            print('Refund was successful!')
            return jsonify(refund.status)
        else:
            print('Refund failed!')
            return jsonify(refund.status)
        # return jsonify(refund)
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True, port=5004)