import firebase_admin
from google.oauth2 import id_token
from google.auth.transport import requests

# credentials = {
#     "apiKey": "AIzaSyCw55Z8cS9e4txG6qPMtNhJBm3SzlnEegE",
#     "authDomain": "poolpal-380405.firebaseapp.com",
#     "projectId": "poolpal-380405",
#     "storageBucket": "poolpal-380405.appspot.com",
#     "messagingSenderId": "61080199721",
#     "appId": "1:61080199721:web:6e4a44fd227444fc52f238",
#     "measurementId": "G-QC3EGJRWJ5"
# }

app = Flask(__name__)

firebase = pyrebase.initialize_app(credentials)
auth = firebase.auth()

app.secret = "secret"


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("trial_files/register.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)

