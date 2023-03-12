from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Create a passenger DB and a Driver DB and a Carpool DB


# Passenger DB

class Passengers(db.Model):
    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PName = db.Column(db.String(200), nullable=False)
    PAge = db.Column(db.Integer, nullable=False)
    PGender = db.Column(db.String(1), nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)
    PAddress = db.Column(db.String(400), nullable=False)
    PPhone = db.Column(db.Integer, nullable=False)
    PAccount_Created_At = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self) -> str:
        return f'Request >>> {self.project}'

# Driver DB

class Drivers(db.Model):
    DID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DName =  db.Column(db.String(200), nullable=False)
    DAge = db.Column(db.Integer, nullable=False)
    DGender = db.Column(db.String(1), nullable=False)
    DEmail = db.Column(db.String(200), nullable=False)
    DAddress = db.Column(db.String(400), nullable=False)
    DVehicleNo = db.Column(db.String(400), nullable=False)
    DLicenseNo = db.Column(db.String(400), nullable=False)
    DPhone = db.Column(db.Integer, nullable=False)
    DAccount_Created_At = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self) -> str:
        return f'Request >>> {self.project}'


# Carpool DB

class Carpool(db.Model):
    CID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DID = db.Column(db.Integer, db.ForeignKey('drivers.DID'), nullable=False)
    PID = db.Column(db.JSON, nullable=True)
    Start_location_lat = db.Column(db.Float, nullable=False)
    Start_Location_long = db.Column(db.Float, nullable=False)
    End_Location_Lat = db.Column(db.Float, nullable=False)
    End_Location_long = db.Column(db.Float, nullable=False)
    Distance = db.Column(db.Float, nullable=False)
    Price = db.Column(db.Float, nullable=True)
    Status = db.Column(db.String(20), nullable=False)
    Created_on = db.Column(db.DateTime, default=datetime.now())

    driver = db.relationship('Drivers', backref=db.backref('carpools', lazy=True))

    def __repr__(self) -> str:
        return f'Carpool >>> {self.CID}'


