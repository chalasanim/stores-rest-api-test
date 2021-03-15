from RestAPI.models.store import StoreModel
from RestAPI.tests.base_test import BaseTest
from RestAPI.models.item import ItemModel
from RestAPI.resources.store import StoreList
import json

class StoreTest(BaseTest):

    def test_create_store(self):
        with self.app as client:
            with self.app_context() :
                resp=client.post('/store/test')
                self.assertEqual(resp.status_code,201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name':'test','items':[]},json.loads(resp.data))


    def test_delete_store(self):
        with self.app as client:
            with self.app_context() :
                 StoreModel('test1').save_to_db()
                 resp=client.delete('/store/test1')
                 self.assertEqual(resp.status_code,200)
                 self.assertDictEqual({'message':'Store deleted'},json.loads(resp.data))



    def test_find_store(self):
        with self.app as client:
            with self.app_context():
                client.post('/store/test')
                resp = client.get('/store/test')
                self.assertEqual(resp.status_code, 200)


    def test_store_not_found(self):
        with self.app as client:
            with self.app_context():
                resp = client.get('/store/test1')
                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual({'message':'Store not found'},json.loads(resp.data))

    def test_create_duplicate_store(self):
        with self.app as client:
            with self.app_context():
                client.post('/store/test')
                resp =  client.post('/store/test')
                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message':"A store with name 'test' already exists."},json.loads(resp.data))

    def test_store_found_with_items(self):
        with self.app as client:
            with self.app_context():
             StoreModel('test').save_to_db()
             ItemModel('dress',19.99,1).save_to_db()
             response=client.get('/store/test',data={'name':'dress'})
             self.assertEqual({'items': [{'name': 'dress', 'price': 19.99}], 'name': 'test'},json.loads(response.data))


    def test_store_with_store_list(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                response=client.get('/stores')
                self.assertDictEqual({'stores':[{'name':'test','items':[]}]},json.loads(response.data))

    def test_store_list_with_items(self):
        with self.app as client:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('dress', 19.99, 1).save_to_db()
                response=client.get('/stores')
                self.assertDictEqual({'stores':[{'name':'test','items':[{'name': 'dress', 'price': 19.99}]}]},json.loads(response.data))











