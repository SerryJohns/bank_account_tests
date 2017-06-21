from unittest import TestCase
from bank_classes.bank import Bank


class TestAccountDeposits(TestCase):
    def setUp(self):
        self.bank = Bank()
        self.account = self.bank.create_account("Account Name", "Savings")

    def test_deposit_successfully(self):
        self.account.deposit(20000)
        self.assertEqual(self.account.balance, 20000)

    def test_deposit_successfully_2(self):
        initial_bal = self.account.balance

        self.account.deposit(20000)
        self.assertEqual(self.account.balance - initial_bal, 20000)

    def test_deposit_with_negative_overdraft(self):
        account_current = self.bank.create_account("Account Name", "Current")
#       Create debt
        account_current.with_draw(1000)
        account_current.deposit(2000)
        self.assertEqual(account_current.balance, 1000)

