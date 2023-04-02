from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'

    feedbackID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phoneNo = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    feedbackDesc = db.Column(db.String(256))



    def __init__(self, username, email, phoneNo, rating, feedbackDesc):
            self.username = username
            self.email = email
            self.phoneNo = phoneNo
            self.rating = rating
            self.feedbackDesc = feedbackDesc
         

    def json(self):
        return {
            "feedbackID": self.feedbackID,
            "username": self.username,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "rating": self.rating,
            "feedbackDesc": self.feedbackDesc,
            }
    

@app.route('/')
def home():
    return render_template("/feedback.html")

@app.route('/api/v1/feedback/create_feedback', methods=['POST'])
def create_feedback():
    #id = request.get_json()['id']
    username = request.json.get('nameInput')
    email = request.json.get('emailInput')
    phoneNo = request.json.get('phoneNoInput')
    rating = request.json.get('ratingInput')
    feedbackDesc = request.json.get('feedbackDesc')
    
    new_feedback = Feedback(
        username,
        email,
        phoneNo,
        rating,
        feedbackDesc
    )


    existing_feedback = Feedback.query.filter_by(email=email).first()
    if existing_feedback:
        return jsonify({
            "code": 400,
            "message": "Feedback already exists."
        }), 400

    

    db.session.add(new_feedback)
    db.session.commit()

    return jsonify(
         {
        "code": 201,
        "data": new_feedback.json()
        }
    ), 201



if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=5008)