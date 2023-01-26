import unittest
from model.Customer import Customer
from repository.CustomerRepository import CustomerRepository


class TestCustomerRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CustomerRepository()
        self.inserted_id = self.repository.insert(Customer(None, "acctnum", "state", 1,"street"))

    def tearDown(self):
        self.repository.delete(Customer(int(self.inserted_id), "acctnum", "state", 1,"street"))

    def test_get(self):
        get_obj: Customer = self.repository.get(
            self.inserted_id)
        self.assertEqual(get_obj.id, int(self.inserted_id))


if __name__ == "__main__":
    unittest.main()