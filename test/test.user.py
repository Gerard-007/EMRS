import unittest
from apps.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("John", "Doe", "1990-01-01", "123 Main St", "555-1234", "john.doe@example.com")

    def test_initialization(self):
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.dob, "1990-01-01")
        self.assertEqual(self.user.address, "123 Main St")
        self.assertEqual(self.user.phone, "555-1234")
        self.assertEqual(self.user.email, "john.doe@example.com")

    def test_str_method(self):
        expected_output = "John Doe, DOB: 1990-01-01, Contact: Address: 123 Main St, Phone: 555-1234, Email: john.doe@example.com"
        self.assertEqual(str(self.user), expected_output)