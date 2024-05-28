import unittest
from main import app

class TestForm(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Form' in response.data)

    def test_form_submission(self):
        tester = app.test_client(self)
        response = tester.post('/', data={
            "name": "Ivan",
            "age": "25",
            "email": "petya228@mail.com",
            "color": "Red",
            "gender": "Female"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Thanks for your reply!' not in response.data)

    def test_thank_you(self):
        tester = app.test_client(self)
        response = tester.get('/thankyou', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Thanks for your reply!' in response.data)

if __name__ == '__main__':
    unittest.main()
