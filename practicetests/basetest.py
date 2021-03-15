from unittest import TestCase
from app import app
from db import db

#This class to be parent class for all the non unit test. It allows to instantiate data bases instantly
#and make sure it is blank in the end and stat


class BaseTest(TestCase):

    def setUp(self) -> None:
        '''Make sure database exist
        # Get a test client'''
        app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app=app.test_client()
        self.app_context=app.app_context()

    def tearDown(self) -> None:
        # database cleans
        with app.app_context():
            db.session.remove()
            db.drop_all()


