from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'

    feedbackID = db.Column(db.Integer, primary_key=True, nullable=False)
    usernmae = db.Column(db.string(100, nullable=False))
    email = db.Column(db.string(100), nullable=False)
    phoneNo = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    feedbackDesc = db.Column(db.String(256))

    def __init__(self, feedbackID, username, email, phoneNo, rating, feedbackDesc):
        self.feedbackID = feedbackID
        self.username = username
        self.email = email
        self.phoneNo = phoneNo
        self.rating = rating
        self.feedbackDesc = feedbackDesc


    def json(self):
        return {"feedbackID": self.feedbackID, 
                "username": self.username,
                "email": self.email, 
                "phoneNo": self.phoneNo, 
                "rating": self.rating, 
                "feedbackDesc": self.feedbackDesc}


# @app.route("/api/v1/feedback/get_all_feedback")
# def get_all():
#     feedbacklist = Feedback.query.all()
#     if len(feedbacklist):
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "feedback": [feedbacks.json() for feedbacks in feedbacklist]
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "There are no feedback."
#         }
#     ), 404


@app.route('/api/v1/feedback/create_feedback/', methods=['POST'])
def create_feedback():
    feedbackID = request.json.get('feedbackID')
    username = request.json.get('username')
    email = request.json.get('email')
    phoneNo = request.json.get('phoneNo')
    rating = request.json.get('rating')
    feedbackDesc = request.json.get('feedbackDesc')

    if (Feedback.query.filter_by(feedbackID=feedbackID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "feedbackID": feedbackID
                },
                "message": "Feedback already exists."
            }
        ), 400

    feedback = Feedback(
        feedbackID=feedbackID,
        username=username,
        email=email,
        phoneNo=phoneNo,
        rating=rating,
        feedbackDesc=feedbackDesc
        )

    try:
        db.session.add(feedback)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "feedbackID": feedbackID
                },
                "message": "An error occurred creating the feedback."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": feedback.json()
        }
    ), 201


# @app.route("/api/v1/review/update_review/<int:CPID>", methods=['PUT'])
# def update_review(CPID):
#     try:
#         review = Review.query.filter_by(CPID=CPID).first()
#         if not review:
#             return jsonify(
#                 {
#                     "code": 404,
#                     "data": {
#                         "CPID": CPID
#                     },
#                     "message": "Review not found."
#                 }
#             ), 404

#          # update multiple columns
#         data = request.get_json()
#         if 'PRating' in data:
#             review.PRating = data['PRating']
#         if 'PDescription' in data:
#             review.PDescription = data['PDescription']

#         if 'DRating' in data:
#             review.DRating = data['DRating']
#         if 'DDescription' in data:
#             review.DDescription = data['DDescription']

#         db.session.commit()

#         return jsonify(
#             {
#                 "code": 200,
#                 "data": review.json()
#             }
#         ), 200
#     except Exception as e:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "CPID": CPID
#                 },
#                 "message": "An error occurred while updating the review. " + str(e)
#             }
#         ), 500

# @app.route("/api/v1/review/find_review/<int:CPID>")
# def find_by_cpid(CPID):
#     review = Review.query.filter_by(CPID=CPID).first()
#     if review:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": review.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message": "Review not found."
#         }
#     ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5008)
