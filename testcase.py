import unittest
from flask import request
from app import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Home Page', response.data)

    def test_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login Page', response.data)

    def test_welcome_route_get(self):
        response = self.app.get('/welcome')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome Page', response.data)

    def test_welcome_route_post(self):
        response = self.app.post('/welcome', data={'password': 'Potatoxyz123!@#'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome Page', response.data)
        self.assertIn(b'test123', response.data)

    def test_result_route_valid_input(self):
        response = self.app.post('/result', data={'search_term': 'safe_input'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result Page', response.data)
        self.assertIn(b'safe_input', response.data)

    def test_result_route_invalid_input_xss(self):
        response = self.app.post('/result', data={'search_term': '<script>alert("XSS")</script>'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)
        self.assertNotIn(b'XSS', response.data)

    def test_result_route_invalid_input_sql_injection(self):
        response = self.app.post('/result', data={'search_term': 'SELECT * FROM users'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)
        self.assertNotIn(b'SELECT', response.data)

if __name__ == '__main__':
    unittest.main()
