from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify  

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop("user")
    
    if request.form['password'] == 'password':
        session['user'] = request.form['username']
        return redirect(url_for('protected'))
    
    return render_template('login.html')

@app.route('/protected')
def protected():
    if g.user:
        render_template('passenger/protected.html', user=session['user'])

    return render_template('login.html')

@app.before_request
def before_request():
    g.user = None 
    if 'user' in session:
        g.user = session['user']
        
@app.route('/dropsession')
def dropsession():
    session.pop("user")
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5400)


