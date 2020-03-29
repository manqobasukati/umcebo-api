from api import api_print
from flask import request, jsonify

from api.get_word_freq import get_word_freq_function

@api_print.route('/token-frequency',methods=['GET'])
def get_word_freq_response():
    word_frequency = get_word_freq_function.get_word_freq_function()
    return jsonify(word_frequency)
