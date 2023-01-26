import unittest
from model.Account import Account
from service.AccountService import AccountService


class TestAccountService(unittest.TestCase):
    def setUp(self):
        print("Setting Up")
        self.service = AccountService()
        #create mock account here

    def tearDown(self):
        print("Tearing Down")
        #delete mock account here


if __name__ == "__main__":
    unittest.main()