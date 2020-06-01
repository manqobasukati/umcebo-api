from api import api_print
from flask import request, jsonify
from flask_cors import cross_origin

from api.get_word_freq import get_word_freq_function


@api_print.route('/get_word_freq_response', methods=['POST'])
@cross_origin()
def get_word_freq_response():


    incoming_resp = [
        {
            "description": "i love banana very much",
            "amount": 50,
            "action":"out"
        },
        {
            "description": "banana",
            "amount": 20,
            "action":"out"

        },
        {
            "description": "chips",
            "amount": 50,
            "action":"out"
        }
    ]

    incoming_json = request.get_json(force=True)
    print(incoming_json)
    word_frequency = get_word_freq_function.get_word_freq_function(incoming=incoming_json)
    return jsonify(word_frequency)
