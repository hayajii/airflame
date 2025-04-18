import unittest
from email_validator import is_valid_email

class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "test@example.com",
            "user.name+tag+sorting@example.com",
            "user@sub.example.com"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "plainaddress",
            "@missingusername.com",
            "username@.com",
            "username@com",
            "username@com.",
            "username@.com.",
            "username@com..com"
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

if __name__ == '__main__':
    unittest.main()