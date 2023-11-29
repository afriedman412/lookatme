from flask_testing import TestCase

from app import app


class TestFolio(TestCase):
    def create_app(self):
        return app

    def test_hello(self):
        response = self.client.get("/hello")
        self.assert200(response)

    def test_home_route(self):
        response = self.client.get("/")
        self.assert200(response)

    def test_render_template_output(self):
        response = self.client.get("/")
        self.assert_template_used("base/about.html")
        self.assertIn(b"They just call me Boo", response.data)

    def test_normy_endpoint(self):
        response = self.client.get("/testo")
        self.assert_template_used("base/page.html")
        self.assertIn(b"Yummy Mummy", response.data)

    def test_alt_endpoint(self):
        response = self.client.get("/work")
        self.assert_template_used("base/page.html")
        self.assertIn(b"Yummy Mummy", response.data)
