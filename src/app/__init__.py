from flask import Flask
from .config import Config
from .auth import auth

def create_app() -> Flask :
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app