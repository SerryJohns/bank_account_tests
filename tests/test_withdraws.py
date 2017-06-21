from unittest import TestCase
from bank_classes.bank import Bank

class TestWithdraws(TestCase):
    def setUp(self):
        self.bank = Bank()
        self.savings_account = self.bank.create_account("Account Name", "Savings")
        self.current_account = self.bank.create_account("Account Name", "Current")

    def test_min_bal_savings(self):
        response = self.savings_account.withdraw(1000)
        self.assertEqual(response, "Can't withdraw below the miminum 1000")

    def test_min_bal_current(self):
        self.current_account.withdraw(3000)
        self.assertEqual(self.current_account.balance, -3000, msg="Account has an overdraft of 3000")

    def test_min_bal_current_over(self):
        response = self.current_account.withdraw(4000)
        self.assertEqual(response, "Account has an over draft of 3000")

    def test_credit_withdraw(self):
        self.savings_account.deposit(10000)
        self.savings_account.withdraw(5000)
        self.assertEqual(self.savings_account.balance, 5000, msg="Account balance should be 5000")

