from flask import render_template, redirect, url_for, flash, session
from . import auth
from app .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    context = {
        'loginForm': loginForm
    }

    if loginForm.validate_on_submit():
        username = loginForm.username.data
        session['username'] = username

        flash('Nombre de usuario guardado!')
        return redirect(url_for('hello'))

    return render_template('login.html', **context)
