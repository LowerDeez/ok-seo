from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory

from ..utils import image_upload_to, get_path_from_request

__all__ = (
    'UtilsTestCase',
)


class UtilsTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('username')

    def test_image_upload_to(self):
        path = image_upload_to(self.user, 'image.jpeg')
        expected_path = f"user/{datetime.now().strftime('%Y/%m/%d')}/image.jpeg"
        self.assertEqual(path, expected_path)

    def test_get_path_from_request(self):
        factory = RequestFactory()
        request = factory.get('/admin/')
        request.path = f'/ru{request.path}'
        path = get_path_from_request(request)
        self.assertEqual(path, '/admin/')
