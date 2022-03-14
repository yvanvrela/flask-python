import uuid
from multiprocessing import context
from flask import (
    render_template, redirect, url_for, flash
)
from flask_login import (
    login_required, login_user, logout_user
)
from werkzeug.security import (
    generate_password_hash, check_password_hash
)
from app.models import (
    UserData, UserModel
)
from . import auth
from app.forms import LoginForm
from app.firestone_service import get_user, user_put


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
            if check_password_hash(password_from_db, password):
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


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Hasta Luego')

    return redirect(url_for('auth.login'))


@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc is None:
            # Genera un id aleatorio
            user_id = str(uuid.uuid4())
            password_hash = generate_password_hash(password)
            user_data = UserData(user_id, username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Bienvenido!')

            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')

    return render_template('signup.html', **context)
