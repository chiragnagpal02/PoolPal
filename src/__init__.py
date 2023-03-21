from flask import Flask, jsonify
import os
from src.carpool import carpool
from src.passengers import passengers
from src.drivers import drivers
from src.googlemap import googleMap
from src.databases import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY'), 
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    
    else:
        app.config.from_mapping(
            test_config
        )

    db.app = app
    db.init_app(app)    

    app.register_blueprint(passengers)
    app.register_blueprint(drivers)
    app.register_blueprint(carpool)
    app.register_blueprint(googleMap)


    
    return app