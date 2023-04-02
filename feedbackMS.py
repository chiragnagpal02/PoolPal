from functools import wraps
from flask import Flask, abort, request, jsonify, render_template
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

    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    phoneNo = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    feedbackDesc = db.Column(db.String(256), nullable=False)


    __table_args__ = (
            db.PrimaryKeyConstraint('id', 'email'),
            {},
    
    )

    def __init__(self, username, email, phoneNo, rating, feedbackDesc):
            self.username = username
            self.email = email
            self.phoneNo = phoneNo
            self.rating = rating
            self.feedbackDesc = feedbackDesc
         

    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phoneNo": self.phoneNo,
            "rating": self.rating,
            "feedbackDesc": self.feedbackDesc,
            }
    

@app.route('/')
def home():
    return render_template("/feedback.html")

# @app.route('/feedback/create', methods=['POST'])
@app.route('/api/v1/feedback/create_feedback', methods=['POST'])
def create_feedback():
    # form_data = json.loads(list(request.form.keys())[0])
    name = request.json.get('nameInput')
    email = request.json.get('emailInput')
    phone_number = request.json.get('phoneNoInput')
    rating = request.json.get('ratingInput')
    feedbackDesc = request.json.get('feedbackDesc')

    # if (Feedback.query.filter_by(email=email).first()):
    #     return jsonify(
    #         {
    #             "code": 400,
    #             "message": "Feedback already exists."
    #         }
    #     ), 400
    
    existing_feedback = Feedback.query.filter_by(email=email).first()
    if existing_feedback:
        return jsonify({
            "code": 400,
            "message": "Feedback already exists."
        }), 400

    new_feedback = Feedback(
        name,
        email,
        phone_number,
        rating,
        feedbackDesc
    )


    db.session.add(new_feedback)
    db.session.commit()

  
    # except:
    #     db.session.rollback()
    #     return jsonify(
    #         {
    #             "code": 500,
    #             "data": {
    #                 "feedbackID": feedback.id
    #             },
    #             "message": "An error occurred creating the feedback."
    #         }
    #     ), 500

    return {
    "code": 201,
    "data": {
        "user_result"
    }
    }


if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=5008)