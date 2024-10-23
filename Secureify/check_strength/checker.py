# Secureify/check_strength/checker.py

from .breach_check import check_breach

def assess_password(password):
    """Assess the strength of a password."""
    if len(password) < 8:
        return "Password is too short."
    if check_breach(password):
        return "Password has been compromised."
    return "Password is strong."