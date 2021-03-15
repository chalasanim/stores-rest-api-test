from starter_code2.starter_code.tests.unit.unit_base_test import  UnitBaseTest
from starter_code2.starter_code.models.store import StoreModel

class StoreTests(UnitBaseTest):

    def create_store(self):
      store=StoreModel("my store")
      self.assertIsNotNone(store)
      self.assertEqual(store.name,'my store')


    def test_json(self):
        store=StoreModel("my store")
        self.assertEqual(store.json(),{'name':'my store','items': []})
        #this is not unit test

