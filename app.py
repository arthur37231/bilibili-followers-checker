from database.base_handler import BaseHandler
from flask import Flask
from flask_cors import CORS
from interface import *
import setting

DEBUG_MODE = True

app = Flask(__name__)
CORS(app)

app.debug = DEBUG_MODE
app.register_blueprint(bili_follower, url_prefix='/api')

app.secret_key = '!@#$%^&*()11'


@app.route('/')
def hello_world():
    return 'Hello Followers Checker!'


def init_model():
    BaseHandler.create_connection(setting.CONF_POSTGRES)


if __name__ == '__main__':
    init_model()
    app.run(
        host='0.0.0.0',
        port=80,
        threaded=True)

