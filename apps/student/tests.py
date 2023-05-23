# Create your tests here.
from django.test import TestCase
from apps.account.models import Account
from apps.donate.models import Donate
from apps.university.models import DEGREE, OTM
from apps.student.models import StudentWallet


class StudentWalletTestCase(TestCase):
    def setUp(self):
        self.student = Account.objects.create(full_name='John Doe', is_student=True, is_active=True)
        self.otm = OTM.objects.create(name='OTM 1')
        self.student_wallet = StudentWallet.objects.create(
            student=self.student,
            degree=DEGREE[0][0],
            otm=self.otm,
            contract_amount=1000.0,
            is_active=True
        )

    def test_student_wallet_fields(self):
        self.assertEqual(self.student_wallet.student, self.student)
        self.assertEqual(self.student_wallet.degree, DEGREE[0][0])
        self.assertEqual(self.student_wallet.otm, self.otm)
        self.assertEqual(self.student_wallet.contract_amount, 1000.0)
        self.assertTrue(self.student_wallet.is_active)
        self.assertIsNotNone(self.student_wallet.date_created)

    def test_str_representation(self):
        expected_str = self.student.full_name
        self.assertEqual(str(self.student_wallet), expected_str)

    def test_donates(self):
        donate1 = Donate.objects.create(student=self.student, donate=200.0)
        donate2 = Donate.objects.create(student=self.student, donate=300.0)

        total_donates = self.student_wallet.donates()
        expected_total_donates = donate1.donate + donate2.donate
        self.assertEqual(total_donates, expected_total_donates)
