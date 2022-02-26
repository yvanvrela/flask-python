from flask import Flask
from flask_login import LoginManager

from app.models import UserModel
from .config import Config
from .auth import auth

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


# Para cuando no haya sesion iniciada
@login_manager.user_loader
def load_user(user_id):
    return UserModel.queryId(user_id)


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(Config)

    login_manager.init_app(app)  # Inicia la app

    app.register_blueprint(auth)

    return app
