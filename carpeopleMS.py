from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/PoolPal'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

CORS(app)

db = SQLAlchemy(app)

class Carpeople(db.Model):
    __tablename__ = 'carpeople'

    CPID = db.Column(db.Integer, nullable=False)
    DID = db.Column(db.Integer, nullable=False)
    PID = db.Column(db.Integer, nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DID', 'PID'),
    )

    def __init__(self, CPID, DID, PID, PEmail):
        self.CPID = CPID
        self.DID = DID
        self.PID = PID
        self.PEmail = PEmail
    
    def json(self):
        return {
            "CPID": self.CPID,
            "DID": self.DID,
            "PID": self.PID,
            "PEmail": self.PEmail
        }
    
@app.route("/api/v1/carpeople/add_passenger", methods=['POST'])
def add_passenger():
    CPID = request.json['CPID']
    DID = request.json['DID']
    PID = request.json['PID']
    PEmail = request.json['PEmail']
    passenger = Carpeople(CPID, DID, PID, PEmail)
    db.session.add(passenger)
    db.session.commit()
    return passenger.json()

@app.route("/api/v1/carpeople/get_all_passengers")
def get_all_passengers():
    passengers = Carpeople.query.all()
    return jsonify([passenger.json() for passenger in passengers])

@app.route("/api/v1/carpeople/get_passengers/<CPID>", methods=['GET'])
def get_passengers(CPID):
    passengers = Carpeople.query.filter_by(CPID=CPID).all()
    return jsonify([passenger.json() for passenger in passengers])

@app.route("/api/v1/carpeople/remove_passenger/<CPID>/<DID>/<PID>", methods=['DELETE'])
def remove_passenger(CPID, DID, PID):
    passenger = Carpeople.query.filter_by(CPID=CPID, DID=DID, PID=PID).first()
    if passenger:
        db.session.delete(passenger)
        db.session.commit()
        return jsonify(
            {
                'code': 200,
                'message': f'Passenger with Email "{passenger.PEmail}" removed from Desired Carpool'
            }
        ), 200
    
    else:
        return jsonify({
            "code": 404,
            "message": "The passenger does not exist."
        }), 404
    
if __name__ == "__main__":
    app.run(debug=True, port=5010, host='0.0.0.0')