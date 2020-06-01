from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'


from api import api_print

app.register_blueprint(api_print)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
