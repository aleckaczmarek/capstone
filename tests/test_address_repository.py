import unittest
from model.Address import Address
from repository.AddressRepository import AddressRepository


class TestAddressRepository(unittest.TestCase):
    def setUp(self):
        self.repository = AddressRepository()
        self.inserted_id = self.repository.insert(Address(None, "acctnum", "state", "sssss","street"))

    def tearDown(self):
        self.repository.delete(Address(int(self.inserted_id), "acctnum", "state", "sssss","street"))

    def test_get(self):
        get_obj: Address = self.repository.get(
            self.inserted_id)
        self.assertEqual(get_obj.id, int(self.inserted_id))


if __name__ == "__main__":
    unittest.main()