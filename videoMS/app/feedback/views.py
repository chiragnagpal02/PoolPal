from flask import Flask, request, jsonify
from . import feedback
from app import db
from app.models import Feedback

import json

@feedback.route('/feedback/create', methods=['POST'])
def create_feedback():
    form_data = json.loads(list(request.form.keys())[0])
    name = form_data['nameInput']
    email = form_data['emailInput']
    phone_number = form_data['phoneNoInput']
    rating = form_data['ratingInput']
    description = form_data['feedbackDesc']

    if (Feedback.query.filter_by(email=email).first()):
        return jsonify(
            {
                "code": 400,
                "message": "Feedback already exists."
            }
        ), 400

    feedback = Feedback(
        name=name,
        email=email,
        phone_number=phone_number,
        rating=rating,
        feedback_description=description
    )

    try:
        db.session.add(feedback)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify(
            {
                "code": 500,
                "data": {
                    "feedbackID": feedback.id
                },
                "message": "An error occurred creating the feedback."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": feedback.json()
        }
    ), 201