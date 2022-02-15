from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)  # Instancia de la app


todos = ['Comprar leche', 'Hacer todo de vuelta', 'Pasar el curso de flask']

# Generar cookies de un usuario


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
    return render_template('hello.html', **context)  # doble asterisco expande todas las variables


# Estructuta de Control


# Debug del servidor
if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
