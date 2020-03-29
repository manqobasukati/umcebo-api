from api import api_print
from flask import request, jsonify

from api.get_word_freq import get_word_freq_function


@api_print.route('/token-frequency', methods=['GET'])
def get_word_freq_response():


    incoming_resp = [
        {
            "description": "i love banana very much",
            "amount": 50
        },
        {
            "description": "banana",
            "amount": 20
        },
        {
            "description": "chips",
            "amount": 50
        }
    ]

    word_frequency = get_word_freq_function.get_word_freq_function(incoming=incoming_resp)
    return jsonify(word_frequency)
