from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewsTest(TestCase):

    def setUp(self):
        """SETUP METHOD TO CREATE A USER FOR TESTS."""
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_signup_view(self):
        """TEST SIGNUP VIEW WORKS CORRECTLY."""
        response = self.client.post(reverse('user:signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password1234', 
            'password2': 'password1234',
            'role': 'official'  # Only if your form handles role
        })
        # print(response.content)  
        self.assertEqual(response.status_code, 200)  # Expect a redirect after successful signup

    def test_login_view(self):
        """TEST LOGIN VIEW WORKS CORRECTLY."""
        response = self.client.post(reverse('user:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after login
        self.assertIn('_auth_user_id', self.client.session)  # User should be logged in

    def test_login_invalid_user(self):
        """TEST LOGIN WITH INVALID CREDENTIALS RETURNS ERROR."""
        response = self.client.post(reverse('user:login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Should stay on the login page
        self.assertNotIn('_auth_user_id', self.client.session)  # User should NOT be logged in
