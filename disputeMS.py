from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS


app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://poolpal@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Dispute(db.Model):
    __tablename__ = 'dispute'

    disputeID = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    CPID = db.Column(db.Integer, nullable=False)
    PID = db.Column(db.Integer, nullable=False)
    DID = db.Column(db.Integer, nullable=False)

    def __init__(self, amount, CPID, PID, DID):
            self.amount = amount
            self.CPID = CPID
            self.PID = PID
            self.DID = DID

    def json(self):
        return {
            "disputeID": self.disputeID,
            "amount": self.amount,
            "CPID": self.CPID,
            "PID": self.PID,
            "DID": self.DID,
            }

@app.route('/api/v1/dispute/create_dispute', methods=['POST'])
def create_dispute():
    #id = request.get_json()['id']
    amount = request.json['amount']
    CPID = request.json['CPID']
    PID = request.json['PID']
    DID = request.json['DID']
    
    new_dispute = Dispute(
        amount,
        CPID,
        PID,
        DID
    )

    db.session.add(new_dispute)
    db.session.commit()

    return jsonify(
         {
        "code": 201,
        "data": new_dispute.json()
        }
    ), 201


if __name__ == '__main__': 
    app.run(host="0.0.0.0", debug=True, port=5125)

