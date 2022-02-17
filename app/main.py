from logging import exception
from flask import Flask, request, make_response, redirect, render_template, abort, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)  # Instancia de la app

app.config['SECRET_KEY'] = 'SECRETO'

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
    userIp = request.remote_addr  # remote_addr -> Trae el ip del usuario
    # Redirecciona a la ruta hello
    response = make_response(redirect('/hello'))
    # response.set_cookie('userIp', userIp)  # vamos a regresar la ip del usuario
    session['userIp'] = userIp

    return response


# Ruta de acceso con un decorador
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    userIp = session.get('userIp')  # Guardar variables encriptadas
    loginForm = LoginForm()
    context = {
        'userIp': userIp,
        'todos': todos,
        'loginForm': loginForm
    }
    # doble asterisco expande todas las variables
    return render_template('hello.html', **context)


# # Debug del servidor
if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
