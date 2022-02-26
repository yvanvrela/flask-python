import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users() -> list:
    """ busca todos los usuarios """
    return db.collection('users').get()


def get_todos(user_id) -> list:
    """ recibe el id, y trae todas las tareas """
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()
