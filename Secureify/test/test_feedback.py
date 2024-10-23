# Secureify/test/test_feedback.py

import unittest
from Secureify.check_strength.feedback import generate_feedback

class TestFeedback(unittest.TestCase):

    def test_feedback(self):
        self.assertEqual(generate_feedback("WeakPass"), "Password is too short.")

if __name__ == '__main__':
    unittest.main()