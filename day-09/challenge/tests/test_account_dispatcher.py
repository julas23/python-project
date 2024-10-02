import unittest
from src.account_dispatcher import AccountDispatcher
from src.account import Account

class TestAccountDispatcher(unittest.TestCase):

    def setUp(self):
        self.dispatcher = AccountDispatcher()
        self.test_account = Account(1)

    def test_add_account(self):
        self.dispatcher.add_account(self.test_account)
        self.assertIn(self.test_account.id, self.dispatcher.accounts)
        self.assertEqual(self.dispatcher.accounts[self.test_account.id], self.test_account)

    def test_get_account_valid(self):
        self.dispatcher.add_account(self.test_account)
        account = self.dispatcher.get_account(self.test_account.id)
        self.assertEqual(account, self.test_account)

    def test_get_account_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.dispatcher.get_account(999)
        self.assertEqual(str(context.exception), "Account 999 not found")

    def test_remove_account_valid(self):
        self.dispatcher.add_account(self.test_account)
        removed_account = self.dispatcher.remove_account(self.test_account.id)
        self.assertEqual(removed_account, self.test_account)
        self.assertNotIn(self.test_account.id, self.dispatcher.accounts)

    def test_remove_account_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.dispatcher.remove_account(999)
        self.assertEqual(str(context.exception), "Account 999 not found")

if __name__ == '__main__':
    unittest.main()