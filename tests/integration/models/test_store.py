from RestAPI.tests.integration.Integreation_base_test import  BaseTest
from RestAPI.models.store import StoreModel
from RestAPI.models.item import ItemModel

class StoreTest(BaseTest):

    def test_item_model_empty(self):
        with self.app_context():
            store = StoreModel("my store")
            item = ItemModel("dress", 19.99, 1)
            self.assertEqual(store.json(), {'name': 'my store', 'items': []})
            self.assertListEqual(store.items.all(),[])

    def test_crud_store(self):

        with self.app_context():

            store=StoreModel("my store")
            self.assertIsNone(store.find_by_name('my store'))

            store.save_to_db()
            self.assertIsNotNone(store.find_by_name('my store'))

            #self.assertEqual(store.json(),{'items':[{'name':'dress','price':19.99}],'name':'my store'})

            store.delete_from_db()
            self.assertIsNone(store.find_by_name('my store'))

    def test_store_relationship(self):

        with self.app_context():
            store=StoreModel('My store')
            item=ItemModel('dress',19.99,1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(),1)
            self.assertEqual(store.items.first().name,'dress')
            self.assertEqual(store.json(),{'items':[{'name':'dress','price':19.99}],'name':'My store'})

    def test_store_json(self):
        with self.app_context():
            store=StoreModel('My Store')
            item=ItemModel('Dress',19.90,1)
            expected={ 'name':'My Store',
                       'items' : []
                    }
            self.assertDictEqual(store.json(),expected)

            store.save_to_db()
            item.save_to_db()
            expected=      expected={ 'name':'My Store',
                       'items' : [{'name':'Dress','price':19.90}]
                    }
            self.assertDictEqual(store.json(),expected)


        #self.assertEqual(store.json(), {'items': [{'name': 'dress', 'price': 19.99}], 'name': 'My store'})

