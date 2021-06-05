from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelClass(TestCase):

    def test_create_user_with_successful_email(self):
        """Test created a user with email successful"""
        email = "test@gmail.com"
        password = "testuser123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """check wheather email is normalized"""
        email = 'mohit@gmail.com'
        user = get_user_model().objects.create_user(email, 'Mohit123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """creating user, with no email, raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Mohit123')

    def test_create_super_user(self):
        """test creating super user"""
        user = get_user_model().objects.create_superuser(
            'mohit@gmai.com',
            'Mohit234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
