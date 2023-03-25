from flask import Flask, render_template, request, jsonify
import stripe


app = Flask(__name__)

stripe_keys = {
  'secret_key': 'sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR',
  'publishable_key': 'pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh'
}

stripe.api_key = stripe_keys["secret_key"]

@app.route('/')
def index():
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/cancelled")
def cancelled():
    return render_template("cancelled.html")

@app.route("/config")
def get_publishable_key():
    stripe_config = {"publicKey": "pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh"}
    return jsonify(stripe_config)

@app.route("/create-checkout-session")
def create_checkout_session():
    domain_url = "http://127.0.0.1:5000/"
    stripe.api_key = "sk_test_51MmIrBFHZFAE1pQVPwD4MzJnsitPPloEFrl3YTqCIiivuil5dTQtRsmKhdnpZn4I7iWtk49Xzp16yEq3Rle2ze9x003p7jB5rR"

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
                'unit_amount': 2000,
                'product_data': {
                    'name': 'PoolPal',
                    'description': 'Your Ride Journey',
                    # 'images': ['https://example.com/t-shirt.png'],
                },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:5000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://127.0.0.1:5000/cancelled',
            )
        return jsonify({"sessionId": checkout_session["id"]})
    except Exception as e:
        print(e)
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(host= "0.0.0.0", debug=True, port=8000)