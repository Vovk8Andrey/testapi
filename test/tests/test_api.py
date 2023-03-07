from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app


class APITestCase(TestCase):
    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_create_image(self):
        image_data = {
            'faces': [{"face_token": "b9bc90fc116f3a0aed92a001a023bd66", "face_rectangle": {"top": 112, "left": 131, "width": 143, "height": 143}, "attributes": {"gender": {"value": "Male"}, "age": {"value": 38}, "ethnicity": {"value": ""}}}],
            'request_id': '1678193879,762408b6-bb2d-4741-9d99-b33112011f6b',
            'image_id': 'igeRWDosEHK02HvGGAB5UA=='
        }
        response = self.client.post('/image', json=image_data)
        self.assertEqual(response.status_code, 200)