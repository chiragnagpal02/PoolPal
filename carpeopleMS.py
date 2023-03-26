from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/PoolPal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

class Carpeople(db.Model):
    __tablename__ = 'carpeople'

    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), autoincrement=True)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passenger.PID'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DID', 'PID'),
    )

    def __init__(self, CPID, DID, PID):
        self.CPID = CPID
        self.DID = DID
        self.PID = PID
    
    def json(self):
        return {
            "CPID": self.CPID,
            "DID": self.DID,
            "PID": self.PID
        }
    