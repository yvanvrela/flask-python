from multiprocessing import context

from flask import render_template
from . import auth
from app.forms import LoginForm


@auth.route('/login')
def login():
    context = {
        'loginForm': LoginForm()
    }
    return render_template('login.html', **context)
