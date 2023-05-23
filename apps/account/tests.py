# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class AccountManagerTestCase(TestCase):
    def test_create_user(self):
        manager = User.objects
        phone = '123456789'
        password = 'password123'
        user = manager.create_user(phone=phone, password=password)

        self.assertEqual(user.phone, phone)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_sponsor)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        manager = User.objects
        phone = '987654321'
        password = 'admin123'
        user = manager.create_superuser(phone=phone, password=password)

        self.assertEqual(user.phone, phone)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_sponsor)
        self.assertTrue(user.is_active)

        # Additional checks for PermissionsMixin
        self.assertTrue(user.has_perm('auth.view_account'))
        self.assertTrue(user.has_perm('auth.change_account'))
        self.assertTrue(user.has_perm('auth.delete_account'))

        # Make sure the user has a token property
        self.assertIsNotNone(user.token)
        self.assertIn('refresh', user.token)
        self.assertIn('access', user.token)


class AccountTestCase(TestCase):
    def test_get_physical_person_count(self):
        User.objects.create(phone='123456789', is_physical_person=True)
        User.objects.create(phone='987654321', is_physical_person=False)

        user = User.objects.first()
        self.assertEqual(user.get_physical_person_count, 1)

    def test_get_legal_entity_count(self):
        User.objects.create(phone='123456789', is_legal_entity=True)
        User.objects.create(phone='987654321', is_legal_entity=False)

        user = User.objects.first()
        self.assertEqual(user.get_legal_entity_count, 1)

    def test_get_student_count(self):
        User.objects.create(phone='123456789', is_student=True)
        User.objects.create(phone='987654321', is_student=False)

        user = User.objects.first()
        self.assertEqual(user.get_student_count(), 1)
