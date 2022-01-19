# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here
    
    def test_read_product_by_id_exists(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertEqual(response.status_code,200)
        self.assertEqual(product["id"],1)
        self.assertEqual(product["name"],"Skello")
    
    def test_read_product_by_id_not_exist(self):
        response = self.client.get("/api/v1/products/6")
        self.assertEqual(response.status_code,404)