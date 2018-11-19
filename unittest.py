from myob import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Flask Unit test case to test endpoint
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code,200)

    # Flask Unit test for verifying the text hello world
    def test_index_hello(self):
        tester=app.test_client(self)
        response=tester.get('/', content_type='html/text')
        self.assertEqual(b'Hello World!', response.data)

    # Flask Unit test case to test health endpoint
    def test_health(self):
        tester = app.test_client(self)
        response = tester.get('/health', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_health_data(self):
        tester = app.test_client(self)
        response = tester.get('/health', content_type='html/text')
        self.assertIn(b'Service Operating Normally', response.data)

    # Flask Unit test case to test metadata endpoint and data validation
    def test_metadata(self):
        tester = app.test_client(self)
        response = tester.get('/metadata', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_metadata_data(self):
        tester = app.test_client(self)
        response = tester.get('/metadata', content_type='html/text')
        self.assertIn(b'myapplication',response.data)
        self.assertIn(b'pre-interview technical test', response.data)


if __name__ == '__main__':
        unittest.main()
