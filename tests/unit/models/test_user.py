from RestAPI.tests.unit.unit_base_test import UnitBaseTest

from RestAPI.models.user import UserModel


class TestUser(UnitBaseTest):

    def test_create_user(self):
        user=UserModel('test_user','test_password')
        self.assertEqual(user.username,'test_user',"User name provided is not taken right")
        self.assertEqual(user.password,'test_password','Password provided is not taken correct')
