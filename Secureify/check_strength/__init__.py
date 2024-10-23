# Secureify/__init__.py

"""
Secureify: A Password Strength Checker

This package provides functionalities to check the strength of passwords
and offer feedback on how to improve them.
"""

# Importing necessary modules/functions for easy access
from .checker import check_strength
from .feedback import get_feedback
from .breach_check import check_breach


__version__ = "0.1.0"
__author__ = "Quadri Basit Ayomide"
