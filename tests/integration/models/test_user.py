from RestAPI.tests.integration.Integreation_base_test import BaseTest
from RestAPI.models.user import UserModel

class UserTest(BaseTest):

    def test_crud(self):

        with self.app_context():

            user=UserModel('test_user','test_pwd')
            self.assertIsNone(user.find_by_name('test_user'))
            self.assertIsNone(user.find_by_id(1))

            user.save_to_db()
            self.assertIsNotNone(user.find_by_name('test_user'))
            self.assertIsNotNone(user.find_by_id(1))



