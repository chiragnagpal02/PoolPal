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


class Staff(db.Model):
    __tablename__ = 'staff'

    SID = db.Column(db.Integer, primary_key=True, nullable=False)
    SName = db.Column(db.String(100), nullable=False)
    Gender = db.Column(db.String(1), nullable=False)

    def __init__(self, SName,Gender):
        #self.SID = SID
        self.SName = SName
        self.Gender = Gender

    def json(self):
        return {"SID": self.SID, "SName": self.SName, "Gender" : self.Gender}


@app.route("/staff")
def get_all():
    stafflist = Staff.query.all()
    if len(stafflist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff": [staff.json() for staff in stafflist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no staff."
        }
    ), 404

@app.route("/staff/<int:SID>")
def find_by_sid(SID):
    staff = Staff.query.filter_by(SID=SID).first()
    if staff:
        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404

@app.route("/create_staff/", methods=['POST'])
def create_staff():
    data = request.get_json()
    staff = Staff(**data)

    try:
        db.session.add(staff)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the staff."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": staff.json()
        }
    ), 201


@app.route("/update_staff/<int:SID>", methods=['PUT'])
def update_staff(SID):
    try:
        staff = Staff.query.filter_by(SID=SID).first()
        if not staff:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "SID": SID
                    },
                    "message": "Staff not found."
                }
            ), 404

         # update multiple columns
        data = request.get_json()
        if 'SName' in data:
            staff.SName = data['SName']

        db.session.commit()

        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "SID": SID
                },
                "message": "An error occurred while updating the staff details. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5007)
