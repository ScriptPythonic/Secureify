# Secureify/__init__.py

"""
Secureify: A Password Strength Checker

This package provides functionalities to check the strength of passwords
and offer feedback on how to improve them.
"""

# Importing necessary modules/functions for easy access
from .breach_check import PasswordBreachChecker
from .checker import PasswordStrengthChecker
from .feedback import provide_strength_feedback



__version__ = "0.1.0"
__author__ = "Quadri Basit Ayomide"
