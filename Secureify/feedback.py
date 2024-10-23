import re

def is_strong_password(password):
    """Checks if the password meets strength criteria."""
    length_criteria = len(password) >= 12
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    return length_criteria and lowercase_criteria and uppercase_criteria and digit_criteria and special_char_criteria

def provide_strength_feedback(password):
    """Provides feedback based on the strength of the password."""
    if is_strong_password(password):
        return "Your password is strong!"
    else:
        return "Your password is weak. Consider using a mix of letters, numbers, and special characters."
