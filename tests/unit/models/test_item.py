from RestAPI.tests.unit.unit_base_test import UnitBaseTest
from RestAPI.models.item import ItemModel



class ItemTest(UnitBaseTest):
    def test_create_item(self):
       item=ItemModel("seeds",2.00,1)
       self.assertEqual(item.name,"seeds","the item name is not matching")
       self.assertEqual(item.price,2.00,"the item price is not matching ")

    def test_json(self):
       item=ItemModel("seeds",2.00,1)
       self.assertEqual(item.json(),{"name":"seeds","price": 2.00}),"Json export of the item is incorrect"

