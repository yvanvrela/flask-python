from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth') # Ingresa la url /auth a todos los auth.

from . import views