from flask import request, make_response, redirect, render_template, abort, session, url_for, flash
import unittest
from app import create_app
from app.forms import LoginForm


app = create_app()

todos = ['Comprar leche', 'Hacer todo de vuelta', 'Pasar el curso de flask']


""" Comandos de testing """


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


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
    response = make_response(redirect('auth/login'))
    # response.set_cookie('userIp', userIp)  # vamos a regresar la ip del usuario

    return response


# Ruta de acceso con un decorador
@app.route('/hello', methods=['GET'])
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



# # Debug del servidor
# if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
