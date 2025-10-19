# exceptions.py
"""
Custom exceptions for Quiz System.
"""

class QuizNotFoundError(Exception):
    """Raised when a quiz ID is invalid or not found."""
    pass

class StudentNotFoundError(Exception):
    """Raised when a student ID is invalid or not found."""
    pass
