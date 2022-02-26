import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users() -> list:
    """ Devuelve todos los usuarios """
    return db.collection('users').get()

def get_user_by_id(user_id):
    return db.collection('users')\
        .document(user_id).get()


def get_user(user_name):
    """Recibe el nombre de usuario, comprueba si existe luego envia los datos"""
    users_from_db = get_users()

    for user in users_from_db:
        if user.to_dict()['username'] == user_name:  # Comprueba si hay un nombre igual
            user_id = user.id
            return db.collection('users')\
                .document(user_id).get()
        else:
            return 


def get_todos(user_id) -> list:
    """ Recibe el id, y devuelve todas las tareas """
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
