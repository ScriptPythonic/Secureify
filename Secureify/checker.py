from .utils import provide_strength_feedback

class PasswordStrengthChecker:
    def check_strength(self, password):
        """Checks the strength of the password."""
        return provide_strength_feedback(password)
