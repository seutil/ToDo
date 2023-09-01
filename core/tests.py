from django.test import SimpleTestCase


class Tests(SimpleTestCase):

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
