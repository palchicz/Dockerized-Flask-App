import unittest

from app import app, db
from models import City

class MainTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)
        db.create_all()
        db.session.add(City('Seattle'))
        db.session.commit()

    def test_data(self):
        response = self.tester.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('SEATTLE!', response.data.decode())

    def test_index(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Flask is running on Docker!')

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
