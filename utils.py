# utils.py
"""
Utility functions.

Functions:
- generate_id(prefix) → e.g., QUIZ-123, QUES-456, STUD-789

  Hint:
- Use uuid.uuid4().hex[:5].upper() for unique IDs.
"""
import uuid

def generate_id(prefix):
    """Generate a unique ID with the given prefix."""
    # Example output: QUIZ-A1B2C
    return f"{prefix}-{uuid.uuid4().hex[:5].upper()}"
