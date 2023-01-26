import unittest
from model.Account import Account
from repository.AccountRepository import AccountRepository


class TestAccountRepository(unittest.TestCase):
    def setUp(self):
        self.accountRepository = AccountRepository()
        self.inserted_account_id = self.accountRepository.insert(Account(None, "acctnum", 1, 25.00))

    def tearDown(self):
        self.accountRepository.delete(Account(int(self.inserted_account_id),"",1,0.0))

    def test_get(self):
        get_account: Account = self.accountRepository.get(
            self.inserted_account_id)
        self.assertEqual(get_account.id, int(self.inserted_account_id))

    def test_update(self):
        get_account: Account = self.accountRepository.get(
            self.inserted_account_id)
        balance_update_check = 15.00
        get_account.updateBalance(balance_update_check)
        self.accountRepository.update(get_account)
        updated_account: Account = self.accountRepository.get(self.inserted_account_id)
        self.assertEqual(updated_account, get_account)

if __name__ == "__main__":
    unittest.main()