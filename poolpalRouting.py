from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/login.html")

@app.route("/driver/homepage")
def about():
    return render_template("driver/driverHomepage1.html")

@app.route("/contact")
def contact():
    return "Here's how to contact me."

if __name__ == "__main__":
    app.run()