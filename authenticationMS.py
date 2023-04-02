import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

app = Flask("Google Login App")
app.secret_key = "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" # make sure this matches with that's in client_secret.json
USERMS_URL = "http://127.0.0.1:5016/api/v1/user"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" # to allow Http traffic for local dev

GOOGLE_CLIENT_ID = "61080199721-is7gst30prt4ar80iahnt1bdquq2gu6b.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5450/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()
    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    next_url = request.args.get("next") or "/"
    return redirect(authorization_url + f"&next={next_url}")


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    # session['id_info'] = id_info
    session['id_info'] = id_info
    session['email'] = id_info.get("email")     
    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["picture"] = id_info.get("picture")

    email_id = session['email']
    url = f"{USERMS_URL}/get_user_by_email/{email_id}"
    response = requests.get(url)
    if response.status_code == 200:
        role = response.json()['data']['Role']
        if role == "Driver":
            return render_template("driver/dHome.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'])
        
        elif role == "Passenger":
            return render_template("passenger/pHome.html", email=session['email'], id_info=session['id_info'], name=session['name'], picture=session['picture'])

    else:
        return render_template("signup.html")

@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['email']}! <br/> <a href='/logout'><button>Logout</button></a>"

# our html pages
@app.route("/")
def index():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/signup")
def signup():
    return render_template("SignUp.html")

# driver
@app.route("/dSignUp")
def dsignup():
    return render_template("driver/dSignUp.html")

@app.route("/dCreateCarpool")
def dCreateCarpool():
    return render_template("driver/dCreateCarpool.html")

@app.route("/dHome")
def dHome():
    return render_template("driver/dHome.html")

@app.route("/dPastRides")
def dPastRides():
    return render_template("driver/dPastRides.html")

@app.route("/dProfile")
def dProfile():
    return render_template("driver/dProfile.html")

@app.route("/dUpcoming")
def dUpcoming():
    return render_template("driver/dUpcoming.html")

# passenger
@app.route("/pSignUp")
def psignup():
    return render_template("passenger/pSignUp.html")

@app.route("/pFindCarpool")
def pFindCarpool():
    return render_template("passenger/pFindCarpool.html")

@app.route("/pHome")
def pHome():
    return render_template("passenger/pHome.html")

@app.route("/pPastRides")
def pPastRides():
    return render_template("passenger/pPastRides.html")

@app.route("/pProfile")
def pProfile():
    return render_template("passenger/pProfile.html")

@app.route("/pUpcoming")
def pUpcoming():
    return render_template("passenger/pUpcoming.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5450, debug=True)