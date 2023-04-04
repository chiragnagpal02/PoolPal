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

class User(db.Model):
    __tablename__ = 'user'

    Email = db.Column(db.String(100), primary_key=True, nullable=False)
    Role = db.Column(db.String(100), nullable=False)

    def __init__(self, Email, Role):
        self.Email = Email
        self.Role = Role

    def json(self):
        return {"Email": self.Email, "Role": self.Role}

@app.route("/api/v1/user/get_all_user")
def get_all():
    userlist = User.query.all()
    if len(userlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "user": [user.json() for user in userlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no user."
        }
    ), 404

@app.route("/api/v1/user/update_user/<string:Email>/<string:Role>", methods=['PUT'])
def update_user(Email,Role):
    try:
        user = User.query.filter_by(Email=Email).first()
        if not user:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "Email": Email
                    },
                    "message": "user not found."
                }
            ), 404

        # update multiple columns
        #data = request.get_json()
        if (Email != ""):
            user.Email = Email
        if (Role != ""):
            user.Role = Role

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Email": Email
                },
                "message": "An error occurred while updating the user. " + str(e)
            }
        ), 500

@app.route("/api/v1/user/get_user_by_email/<string:Email>")
def find_user_by_email(Email):
    user = User.query.filter_by(Email=Email).first()
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "User not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5016)