import unittest
from unittest.mock import patch
from Secureify.breach_check import PasswordBreachChecker

class TestPasswordBreachChecker(unittest.TestCase):
    def setUp(self):
        self.breach_checker = PasswordBreachChecker()

    @patch('Secureify.breach_check.requests.get')
    def test_password_not_breached(self, mock_get):
        # Mocking the API response for a non-breached password
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "ABC123:100\nDEF456:50"
        
        result = self.breach_checker.check_breach("SafePassword123!")
        self.assertEqual(result, "This password has not been found in any data breaches.")

    @patch('Secureify.breach_check.requests.get')
    def test_password_breached(self, mock_get):
        # Mocking the API response for a breached password
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "ABC123:100\nSafePassword123!:200"
        
        result = self.breach_checker.check_breach("SafePassword123!")
        self.assertEqual(result, "This password has been exposed 200 times in data breaches.")

if __name__ == "__main__":
    unittest.main()
