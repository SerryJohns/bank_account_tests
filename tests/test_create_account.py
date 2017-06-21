from unittest import TestCase
from bank_classes.bank import Bank
from bank_classes.account import Savings, Current

class TestCreateBankAccount(TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_create_account_successfully(self):
        new_account = self.bank.create_account("Account Name", "Savings")
        self.assertTrue(new_account, msg="New Account should be created")

    def test_create_account_savings(self):
        new_account = self.bank.create_account("Account Name", "Savings")
        self.assertIsInstance(new_account, Savings, msg="Account should be an instance of Savings")

    def test_savings_min_balance(self):
        new_account = self.bank.create_account("Account Name", "Savings")
        self.assertEqual(new_account.min_balance, 1000, msg="Minimum balance should be 1000")

    def test_create_account_current(self):
        new_account = self.bank.create_account("Account Name", "Current")
        self.assertIsInstance(new_account, Savings, msg="Account should be an instance of Current")

    def test_current_min_balance(self):
        new_account = self.bank.create_account("Account Name", "Current")
        self.assertEqual(new_account.min_balance, -3000, msg="Should have an overdraft of 3000")

    def test_wrong_account_type(self):
        new_account = self.bank.create_account("Account Name", "SomeType")
        self.assertRaises(TypeError)
