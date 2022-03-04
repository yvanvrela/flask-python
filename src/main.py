import unittest
from flask import(
    flash, make_response, redirect, render_template, url_for
)
from app import create_app
from app.firestone_service import get_todos, put_todo
from flask_login import login_required, current_user

from app.forms import TodoForm


app = create_app()


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

    return response


# Ruta de acceso con un decorador
@app.route('/hello', methods=['GET', 'POST'])
@login_required  # Autenticacion del login
def hello():
    user_id = current_user.id
    username = current_user.username
    todo_form = TodoForm()

    # Diccionario de retorno de los datos a la pagina
    context = {
        'todos': get_todos(user_id),  # lista de tareas
        'username': username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=user_id, description=todo_form.description.data)

        flash('Todo agregado!')

        return redirect(url_for('hello'))

    # doble asterisco expande todas las variables
    return render_template('hello.html', **context)


# # Debug del servidor
# if __name__ == '__main__':
    app.run(host='localhost', port=4000, debug=True)
