from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    def test_create(self):
        tester= app.test_client(self)
        response = tester.get(r'/create_Contact/test/test/test/78899',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_retrieve(self):
        tester = app.test_client(self)
        response = tester.get(r'/get_Contact/test',content_type='html/text')
        self.assertEqual(response.status_code,201)

    def test_retrieve(self):
        tester = app.test_client(self)
        response = tester.get(r'/update_Contact/test/78899',content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_retrieve(self):
        tester = app.test_client(self)
        response = tester.get(r'/delete_Contact/test',content_type='html/text')
        self.assertEqual(response.status_code,200)
        


                              
                            
