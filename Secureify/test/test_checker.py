# Secureify/test/test_checker.py

import unittest
from Secureify.check_strength.checker import assess_password

class TestPasswordChecker(unittest.TestCase):

    def test_short_password(self):
        self.assertEqual(assess_password("12345"), "Password is too short.")

    def test_strong_password(self):
        self.assertEqual(assess_password("StrongP@ssw0rd"), "Password is strong.")

if __name__ == '__main__':
    unittest.main()