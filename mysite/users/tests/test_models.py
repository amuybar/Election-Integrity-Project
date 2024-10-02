from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class CustomUserModelTest(TestCase):

    def setUp(self):
        # This method will run before each test
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            role='citizen'  # Ensure this is a valid role
        )

    def test_user_creation(self):
        """Test that a user can be created with the right attributes."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password123'))
        self.assertEqual(self.user.role, 'citizen')

    def test_invalid_role(self):
        """Test that an invalid role raises a validation error."""
        with self.assertRaises(ValidationError):
            user = User(username='invaliduser', password='password123', role='invalid_role')
            user.full_clean()  # This should raise a ValidationError

    def test_user_str(self):
        """Test the string representation of the user."""
        self.assertEqual(str(self.user), 'testuser')  # Assuming __str__ returns username

    def test_user_role_choices(self):
        """Test that user roles are valid choices."""
        valid_roles = ['citizen', 'monitor', 'official']
        self.assertIn(self.user.role, valid_roles)

    def test_user_update(self):
        """Test that user attributes can be updated."""
        self.user.role = 'monitor'
        self.user.save()
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.role, 'monitor')
