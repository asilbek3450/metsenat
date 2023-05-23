# Create your tests here.
from django.test import TestCase
from django.utils import timezone
from apps.donate.models import Donate
from apps.sponsor.models import SponsorWallet
from apps.student.models import StudentWallet


class DonateTestCase(TestCase):
    def setUp(self):
        self.sponsor_wallet = SponsorWallet.objects.create()  # Create a SponsorWallet instance
        self.student_wallet = StudentWallet.objects.create()  # Create a StudentWallet instance
        self.donate = Donate.objects.create(
            sponsor=self.sponsor_wallet,
            student=self.student_wallet,
            donate=100.0,
            date_created=timezone.now()
        )

    def test_donate_fields(self):
        self.assertEqual(self.donate.sponsor, self.sponsor_wallet)
        self.assertEqual(self.donate.student, self.student_wallet)
        self.assertEqual(self.donate.donate, 100.0)
        self.assertIsNotNone(self.donate.date_created)

    def test_str_representation(self):
        expected_str = str(self.donate.donate)
        self.assertEqual(str(self.donate), expected_str)
