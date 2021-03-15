from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
       item=ItemModel("seeds","2.00")
       self.assertEqual(item.name,"seeds","the item name is not matching")
       self.assertEqual(item.price,"2.00","the item price is not matching ")

    def test_json(self):
        item=ItemModel("seeds","2.00")
        self.assertEqual(item.json(),{"name":"seeds","price": "2.00"}),"Json export of the item is incorrect"

