from practicetests.basetest import BaseTest
from models.item import ItemModel

class ItemTest(BaseTest):

    def test_crud(self):

       with self.app_context:
          item =ItemModel("seeds", "2.00")
          self.assertIsNone(ItemModel.find_by_name("seeds"))

          item.save_to_db()
          self.assertIsNotNone(ItemModel.find_by_name("seeds"))

          item.delete_from_db()
          self.assertIsNone(ItemModel.find_by_name("seeds"))

