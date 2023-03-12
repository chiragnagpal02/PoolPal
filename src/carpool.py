from flask import Blueprint, jsonify


carpool = Blueprint('carpool', __name__, url_prefix='/api/v1/carpool')


@carpool.route('/register', methods=['POST'])
def create_carpool():
    return {'message': 'User Created'}


@carpool.route('/me')
def me():
    return {'message': 'User Me'}
