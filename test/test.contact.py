import unittest
from apps.contact import ContactInfo


class TestContactInfo(unittest.TestCase):
    def setUp(self):
        self.contact_info = ContactInfo("123 Semicolon St", "08062134747", "test@example.com")

    def test_initialization(self):
        self.assertEqual(self.contact_info.address, "123 Semicolon St")
        self.assertEqual(self.contact_info.phone, "08062134747")
        self.assertEqual(self.contact_info.email, "test@example.com")

    def test_str_method(self):
        expected_output = "Address: 123 Semicolon St, Phone: 08062134747, Email: test@example.com"
        self.assertEqual(str(self.contact_info), expected_output)
