from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user
from app.models import UserData, UserModel
from . import auth
from app.forms import LoginForm
from app.firestone_service import get_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    context = {
        'loginForm': loginForm
    }

    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data

        user_doc = get_user(username)

        if user_doc is not None:
            # Se extrae el valor del password
            password_from_db = user_doc.to_dict()['password']
            user_id_from_db = user_doc.id

            # Comprueba si coinciden los passwords
            if password == password_from_db:
                user_id = user_id_from_db

                user_data = UserData(user_id, username, password)
                user = UserModel(user_data)
                login_user(user)
                flash('Bienvenido')

                return redirect(url_for('hello'))
            else:
                flash('Contraseña incorrecta')
        else:
            flash('El usuario no existe')

    return render_template('login.html', **context)
