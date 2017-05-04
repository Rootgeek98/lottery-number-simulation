from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from . import main
    app.register_blueprint(main.main)

    return app
