from flask import Flask, request, make_response, redirect

app = Flask(__name__)  # Instancia de la app


# Generar cookies de un usuario
@app.route('/')
def index():
    userIp = request.remote_addr  # remote_addr -> Trae el ip del usuario
    response = make_response(redirect('/hello')) # Redirecciona a la ruta hello
    response.set_cookie('userIp', userIp) # vamos a regresar la ip del usuario

    return response


@app.route('/hello')  # Ruta de acceso con un decorador
def hello():
    userIp = request.cookies.get('userIp')
    return f'Tu ip es: {userIp}'


# Debug del servidor
if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
