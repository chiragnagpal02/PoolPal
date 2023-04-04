from flask import Blueprint

feedback = Blueprint('feedback', '__init__')

from . import views
