from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def retreive():
    return render_template('/passenger/passengerRideOffers.html') 

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5003)