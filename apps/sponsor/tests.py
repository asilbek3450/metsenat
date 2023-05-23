# Create your tests here.
from django.test import TestCase
from apps.account.models import Account
from apps.donate.models import Donate
from apps.university.models import STATUS
from apps.sponsor.models import SponsorWallet


class SponsorWalletTestCase(TestCase):
    def setUp(self):
        self.sponsor = Account.objects.create(phone='123456789', is_sponsor=True, is_active=True)
        self.sponsor_wallet = SponsorWallet.objects.create(
            sponsor=self.sponsor,
            sponsor_wallet=1000.0,
            spent_amount=500.0,
            status=STATUS[0][0],
            is_active=True
        )

    def test_sponsor_wallet_fields(self):
        self.assertEqual(self.sponsor_wallet.sponsor, self.sponsor)
        self.assertEqual(self.sponsor_wallet.sponsor_wallet, 1000.0)
        self.assertEqual(self.sponsor_wallet.spent_amount, 500.0)
        self.assertEqual(self.sponsor_wallet.status, STATUS[0][0])
        self.assertTrue(self.sponsor_wallet.is_active)
        self.assertIsNotNone(self.sponsor_wallet.date_created)

    def test_str_representation(self):
        expected_str = self.sponsor.phone
        self.assertEqual(str(self.sponsor_wallet), expected_str)

    def test_spent_amounts(self):
        donate1 = Donate.objects.create(sponsor=self.sponsor, donate=200.0)
        donate2 = Donate.objects.create(sponsor=self.sponsor, donate=300.0)

        spent_amount = self.sponsor_wallet.spent_amounts()
        expected_spent_amount = self.sponsor_wallet.sponsor_wallet - donate1.donate - donate2.donate
        self.assertEqual(spent_amount, expected_spent_amount)

    def test_wallet_avg(self):
        donate1 = Donate.objects.create(sponsor=self.sponsor, donate=200.0)
        donate2 = Donate.objects.create(sponsor=self.sponsor, donate=300.0)

        wallet_avg = self.sponsor_wallet.wallet_avg()
        expected_wallet_avg = donate1.donate + donate2.donate
        self.assertEqual(wallet_avg, expected_wallet_avg)
