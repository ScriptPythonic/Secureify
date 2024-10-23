import unittest
from Secureify.checker import PasswordStrengthChecker
from Secureify.utils import provide_strength_feedback

class TestPasswordStrengthChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    def test_strong_password(self):
        password = "Str0ngP@ssw0rd!"
        result = self.checker.check_strength(password)
        self.assertIn("strong", result)

    def test_weak_password(self):
        password = "12345"
        result = self.checker.check_strength(password)
        self.assertIn("weak", result)

    def test_medium_password(self):
        password = "P@ssword123"
        result = self.checker.check_strength(password)
        self.assertIn("medium", result)

if __name__ == "__main__":
    unittest.main()
