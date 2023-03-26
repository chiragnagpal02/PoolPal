from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


db = SQLAlchemy(app)
CORS(app)


class Review(db.Model):
    __tablename__ = 'review'

    CPID = db.Column(db.Integer, primary_key=True, nullable=False)
    DID = db.Column(db.Integer, nullable=False)
    PID = db.Column(db.Integer, nullable=False)
    PRating = db.Column(db.Integer)
    DRating = db.Column(db.Integer)
    PDescription = db.Column(db.String(100))
    DDescription = db.Column(db.String(100))

    def __init__(self, CPID, DID, PID, PRating, DRating, PDescription, DDescription):
        self.CPID = CPID
        self.DID = DID
        self.PID = PID
        self.PRating = PRating
        self.DRating = DRating
        self.PDescription = PDescription
        self.DDescription = DDescription

    def json(self):
        return {"CPID": self.CPID, "DID": self.DID, "PID": self.PID, "PRating": self.PRating, "DRating": self.DRating, "PDescription": self.PDescription, "DDescription": self.DDescription}


@app.route("/api/v1/review/get_all_reviews")
def get_all():
    reviewlist = Review.query.all()
    if len(reviewlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "review": [review.json() for review in reviewlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no reviews."
        }
    ), 404


@app.route("/api/v1/review/create_review/<int:CPID>", methods=['POST'])
def create_review(CPID):
    if (Review.query.filter_by(CPID=CPID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "CPID": CPID
                },
                "message": "Review already exists."
            }
        ), 400

    data = request.get_json()
    review = Review(CPID, **data)

    try:
        db.session.add(review)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "CPID": CPID
                },
                "message": "An error occurred creating the review."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": review.json()
        }
    ), 201


@app.route("/api/v1/review/update_review/<int:CPID>", methods=['PUT'])
def update_review(CPID):
    try:
        review = Review.query.filter_by(CPID=CPID).first()
        if not review:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "CPID": CPID
                    },
                    "message": "Review not found."
                }
            ), 404

         # update multiple columns
        data = request.get_json()
        if 'PRating' in data:
            review.PRating = data['PRating']
        if 'PDescription' in data:
            review.PDescription = data['PDescription']

        if 'DRating' in data:
            review.DRating = data['DRating']
        if 'DDescription' in data:
            review.DDescription = data['DDescription']

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": review.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "CPID": CPID
                },
                "message": "An error occurred while updating the review. " + str(e)
            }
        ), 500

@app.route("/api/v1/review/find_review/<int:CPID>")
def find_by_cpid(CPID):
    review = Review.query.filter_by(CPID=CPID).first()
    if review:
        return jsonify(
            {
                "code": 200,
                "data": review.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Review not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5006)
