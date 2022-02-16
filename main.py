from logging import exception
from flask import Flask, request, make_response, redirect, render_template, abort

app = Flask(__name__)  # Instancia de la app


todos = ['Comprar leche', 'Hacer todo de vuelta', 'Pasar el curso de flask']


""" Manejos de errores"""


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def not_found(error):
    return render_template('500.html', error=error) # se debe usar una variable abort o que nada funcione


@app.route('/')
def index():
    userIp = request.remote_addr  # remote_addr -> Trae el ip del usuario
    # Redirecciona a la ruta hello
    response = make_response(redirect('/hello'))
    response.set_cookie('userIp', userIp)  # vamos a regresar la ip del usuario

    return response


@app.route('/hello')  # Ruta de acceso con un decorador
def hello():
    userIp = request.cookies.get('userIp')
    context = {
        'userIp': userIp,
        'todos': todos
    }
    # doble asterisco expande todas las variables
    return render_template('hello.html', **context)


# # Debug del servidor
# if __name__ == '__main__':
#     app.run(host='localhost', port=4000, debug=True)
