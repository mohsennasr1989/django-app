from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Tag


def sample_user(email='test@domain.com', password='testPass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating user with email is successful"""
        email = "test@domain.com"
        password = "testPass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test user email is normalized"""
        email = 'test@domain.com'
        user = get_user_model().objects.create_user(email, 'testPass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testPass')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects \
            .create_superuser('test@domain.com', 'testPass')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string representation"""
        tag = Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)
