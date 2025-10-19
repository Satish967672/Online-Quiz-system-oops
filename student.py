# student.py
"""
Student class representing a quiz taker.

Attributes:
- student_id (str)
- name (str)
- quiz_scores (dict → {quiz_id: score})

Methods:
- record_score(quiz_id, score)
- __str__() → print student summary

💡 Hint:
- Use a dictionary to store multiple quiz attempts.
"""

class Student:
    def __init__(self, student_id, name):
        # Initialize student attributes
        self.student_id = student_id
        self.name = name
        self.quiz_scores = {}

    def record_score(self, quiz_id, score):
        """
        Record a student's quiz score.
        Hint: self.quiz_scores[quiz_id] = score
        """
        self.quiz_scores[quiz_id] = score

    def __str__(self):
        """
        Return student_id + name + number of quizzes attempted.
        """
        return f"Student [{self.student_id}] - {self.name} | Quizzes attempted: {len(self.quiz_scores)}"
