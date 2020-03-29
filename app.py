from flask import Flask

app = Flask(__name__)


from api import api_print

app.register_blueprint(api_print)

if __name__ == '__main__':
    app.run(debug=True)