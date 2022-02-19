from urllib import response
from urllib.request import urlretrieve
from flask_testing import TestCase
from flask import current_app, url_for  # la app que ejecutamos

from src.main import app


# se crea una clase que extiende TestCase
class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLE'] = False  # Para no hacer los WTF
        app.config['DEBUG'] = False

        return app

    def testAppExists(self):  # app existe
        self.assertIsNotNone(current_app)

    def testAppInTestMode(self):
        self.assertTrue(current_app.config['TESTING'])

    def testIndexRedirect(self):
        response = self.client.get(url_for('index'))

        # Compara si la redireccion es igual al response
        self.assertRedirects(response, url_for('login'))

    def testLoginPost(self):
        fakeForm = {
            'username': 'fake',
            'password': 'fakePassword'
        }
        response = self.client.post(url_for('login'), data=fakeForm)

        self.assertRedirects(response, url_for('hello'))
