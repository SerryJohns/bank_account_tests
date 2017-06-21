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
        self.account.deposit(7000)
        current_bal = self.account.balance

        self.account.deposit(20000)
        self.assertEqual(self.account.balance - current_bal, 20000)
        
    def test_deposit_successfully_with_message(self):
        response = self.account.deposit(3000)
        self.assertEqual(response, "Account credited successfully, your account balance is now {}".format(self.account.balance))

    def test_deposit_with_debt(self):
        account_current = self.bank.create_account("Account Name", "Current")
#       Create debt
        account_current.with_draw(1000)
        account_current.deposit(2000)
        self.assertEqual(account_current.balance, 1000)

