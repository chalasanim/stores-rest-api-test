from RestAPI.tests.integration.Integreation_base_test import BaseTest
from RestAPI.models.item import ItemModel
from RestAPI.models.store import StoreModel

class ItemTest(BaseTest):

    def test_crud(self):

       with self.app_context():
          StoreModel("seeds").save_to_db()
          item =ItemModel("beans", 2.00,1)
          self.assertIsNone(ItemModel.find_by_name("beans"))

          item.save_to_db()
          self.assertIsNotNone(ItemModel.find_by_name("beans"))

          item.delete_from_db()
          self.assertIsNone(ItemModel.find_by_name("seeds"))

    def test_store_relationship(self):
       with self.app_context():
          store=StoreModel("seed store")
          item=ItemModel("beans",2.00,1)
          store.save_to_db()
          item.save_to_db()
          self.assertEqual(item.store.name,"seed store")
          self.assertEqual(store.id,1)

