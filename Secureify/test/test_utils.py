# Secureify/test/test_utils.py

import unittest
from Secureify.check_strength.utils import is_strong_password

class TestUtils(unittest.TestCase):

    def test_is_strong_password(self):
        self.assertTrue(is_strong_password("StrongP@ssw0rd"))
        self.assertFalse(is_strong_password("short"))

if __name__ == '__main__':
    unittest.main()