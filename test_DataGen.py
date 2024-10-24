import unittest
from DataGen import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_physical_data(self):
        response = self.app.post('/generate', json={'type': 'physical'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

    def test_generate_climate_data(self):
        response = self.app.post('/generate', json={'type': 'climate'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

    def test_generate_biological_data(self):
        response = self.app.post('/generate', json={'type': 'biological'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

if __name__ == '__main__':
    unittest.main()
