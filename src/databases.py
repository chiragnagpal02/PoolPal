from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Creating all the individual Tables inside the db Database -> Each MS to have its own Schema 
class Driver(db.Model):
    __tablename__ = 'driver'

    DID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DName = db.Column(db.String(64), nullable=False)
    DGender = db.Column(db.String(1), nullable=False)
    DEmail = db.Column(db.String(64), nullable=False)
    DVehicleNo = db.Column(db.String(64), nullable=False)
    DLicenseNo = db.Column(db.String(64), nullable=False)
    DLicenseExpiration = db.Column(db.DateTime, nullable=True)
    DPhoneNo = db.Column(db.Integer, nullable=False)
    DCar = db.Column(db.String(100), nullable=False)
    DCapacity = db.Column(db.Integer, nullable=False)


# Passenger DB

class Passengers(db.Model):
    PID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PName = db.Column(db.String(200), nullable=False)
    PUserName = db.Column(db.String(200), nullable=False, unique=True)
    PAge = db.Column(db.Integer, nullable=False)
    PGender = db.Column(db.String(1), nullable=False)
    PEmail = db.Column(db.String(200), nullable=False)
    PAddress = db.Column(db.String(400), nullable=False)
    PPhone = db.Column(db.Integer, nullable=False)
    PAccount_Created_At = db.Column(db.DateTime, default=datetime.now())
    
    
    def __repr__(self) -> str:
        return f'Request >>> {self.project}'
    
# Carpool DB
class Carpool(db.Model):
    __tablename__ = 'carpooling'

    CPID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    DriverFee = db.Column(db.Float(precision=2), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    CPStartLocation = db.Column(db.String(64), nullable=False)
    CPendLocation = db.Column(db.String(64), nullable=False)
    Status = db.Column(db.String(64), nullable=False)
    Price = db.Column(db.Float(precision=2), nullable=False)
    Capacity = db.Column(db.Integer, nullable=False)


# This is for seeing the people who are registering for a particular carpool
class CarPeople(db.Model):
    __tablename__ = 'carpeople'
    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), nullable=False)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passengers.PID'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'PID', ),
    )

# Review DB
class Review(db.Model):
    __tablename__ = 'review'

    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passengers.PID'), nullable=False)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    #DateTime = db.Column(db.DateTime, default=datetime.now())
    PRating = db.Column(db.Integer)
    DRating = db.Column(db.Integer)
    PDescription = db.Column(db.String(100))
    DDescription = db.Column(db.String(100))

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'PID', 'DID'),
    )

# Dispute DB

class Dispute(db.Model):
    __tablename__ = 'dispute'

    DPID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passengers.PID'), nullable=False)
    DID = db.Column(db.Integer, db.ForeignKey('driver.DID'), nullable=False)
    SID = db.Column(db.Integer, nullable=False)
    DPDescript = db.Column(db.String(64), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())

# Payment Log DB

class PaymentLog(db.Model):
    __tablename__ = 'PaymentLog'

    PmID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    CPID = db.Column(db.Integer, db.ForeignKey('carpooling.CPID'), nullable=False)
    PID = db.Column(db.Integer, db.ForeignKey('passengers.PID'), nullable=False)
    CPrice = db.Column(db.Float(precision=2), nullable=False)
    Status = db.Column(db.String(64), nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())

# Staff DB
class Staff(db.Model):
    __tablename__ = 'staff'

    SID = db.Column(db.Integer, primary_key=True, nullable=False)
    SName = db.Column(db.String(100), nullable=False)
    Gender = db.Column(db.String(1), nullable=False)

# Pricing DB
class Pricing(db.Model):
    __tablename__ = 'pricing'

    CPID = db.Column(db.Integer, nullable=False)
    DateTime = db.Column(db.DateTime, default=datetime.now())
    OriginalPrice = db.Column(db.Float(precision=2), nullable=False)
    CPrice = db.Column(db.Float(precision=2), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('CPID', 'DateTime'),
    )

