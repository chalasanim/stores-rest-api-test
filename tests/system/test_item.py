from RestAPI.models.store import StoreModel
from RestAPI.tests.base_test import BaseTest
from RestAPI.models.item import ItemModel
from RestAPI.models.user import UserModel
from RestAPI.resources.item import ItemList
import json

class ItemTest(BaseTest):

    def test_get_item_no_auth(self):
        with self.app as client:
            with self.app_context() :
                response=client.get('/item/test')

    def test_get_item_not_found(self):
        pass

    def test_get_item(self):
        pass

    def test_create_item(self):
        pass

    def test_duplicate_item(self):
        pass

    def test_put_item(self):
        pass

    def test_post_item(self):
        pass

    def test_delete_item(self):
        pass
