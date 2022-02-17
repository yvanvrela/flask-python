from logging import exception
from flask import Flask, request, make_response, redirect, render_template, abort, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)  # Instancia de la app

app.config['SECRET_KEY'] = 'SECRETO'
app.config['WTF_CSRF_ENABLED'] = False

todos = ['Comprar leche', 'Hacer todo de vuelta', 'Pasar el curso de flask']

# Clase para los login


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
                           DataRequired()])  # Validar los datos
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


""" Manejos de errores"""


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    # se debe usar una variable abort o que nada funcione
    return render_template('500.html', error=error)


@app.route('/')
def index():

    # Redirecciona a la ruta hello
    response = make_response(redirect('/login'))
    # response.set_cookie('userIp', userIp)  # vamos a regresar la ip del usuario

    return response


# Ruta de acceso con un decorador
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    userIp = session.get('userIp')  # Guardar variables encriptadas
    username = session.get('username')

    # Diccionario de retorno de los datos
    context = {
        'userIp': userIp,
        'todos': todos,  # lista de tareas
        'username': username
    }

    # doble asterisco expande todas las variables
    return render_template('hello.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    userIp = request.remote_addr  # remote_addr -> Trae el ip del usuario
    session['userIp'] = userIp

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

# # Debug del servidor
# if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
