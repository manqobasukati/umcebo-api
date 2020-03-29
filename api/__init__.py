from flask import Blueprint

api_print = Blueprint('api_print', __name__, url_prefix='/api/v1/')

from api.get_word_freq.get_word_freq_response import *