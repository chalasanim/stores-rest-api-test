from RestAPI.tests.base_test import BaseTest
from RestAPI.models.user import UserModel
import RestAPI.security
import json

class UserTest(BaseTest):

    # test register user
    # test user login
    # test duplicate user

    def test_register_user(self):
        with self.app as client:
            with self.app_context():
              response = client.post('/register', data={'username':'firstuser1','password':'123'})

              self.assertEqual(response.status_code,201)
              self.assertIsNotNone(UserModel.find_by_name('firstuser1'))
              self.assertDictEqual({'message': 'User created with the inputs provided'},json.loads(response.data))


    def test_login_user(self):
        with self.app as client:
            with self.app_context():
                data1 = {'username': 'firstuser', 'password': '1234'}
                data=json.dumps(data1)

                client.post('/register',data=data1)

                auth_response=client.post('/auth',
                                         data=data,
                                         headers={'content-type': 'application/json'})

                self.assertIn('access_token',json.loads(auth_response.data).keys())

    def test_duplicate_user(self):
        with self.app as client:
            with self.app_context():
                client.post('/register', data={'username': 'firstuser', 'password': '123'})

                response = client.post('/register', data={'username': 'firstuser', 'password': '123'})
                self.assertEqual(response.status_code,400)
                self.assertIsNotNone(UserModel.find_by_name('firstuser'))
                self.assertDictEqual({'message': 'User with name allready exist'},json.loads(response.data))
