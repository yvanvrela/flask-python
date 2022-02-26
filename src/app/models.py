from flask_login import UserMixin
from .firestone_service import get_user, get_user_by_id


class UserData:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """UserData"""
        self.id = user_data.user_id
        self.username = user_data.username
        self.password = user_data.password

    @staticmethod  # no recibe self
    def query(user_name):
        user_doc = get_user(user_name)  # Trae el usuario, si existe

        # Nueva instancia de UserData, busca en la bd si existe el usuario
        user_data = UserData(
            user_id=user_doc.id,
            username=user_doc.to_dict()['username'],
            password=user_doc.to_dict()['password']
        )

        return UserModel(user_data)

    @staticmethod  # no recibe self
    def queryId(user_id):
        user_doc = get_user_by_id(user_id)  # Trae el usuario, si existe

        # Nueva instancia de UserData, busca en la bd si existe el usuario
        user_data = UserData(
            user_id=user_doc.id,
            username=user_doc.to_dict()['username'],
            password=user_doc.to_dict()['password']
        )

        return UserModel(user_data)
