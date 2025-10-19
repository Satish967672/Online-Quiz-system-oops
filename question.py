# question.py
"""
Question class for multiple-choice quiz.

Attributes:
- question_id (str)
- text (str)
- options (list of str)
- correct_answer (str)

Methods:
- check_answer(answer) → returns True/False
- __str__() → nicely prints the question and options

💡 Hint:
- Store options as a list ["A. ...", "B. ...", "C. ...", "D. ..."]
- correct_answer should match one option letter (A/B/C/D)
"""

class Question:
    def __init__(self, question_id, text, options, correct_answer):
        # Initialize question attributes
        self.question_id = question_id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, answer):
        """
        Check if the provided answer matches the correct answer.
        Hint: Compare after stripping and converting to uppercase.
        """
        return answer.strip().upper() == self.correct_answer.strip().upper()

    def __str__(self):
        """
        String representation of the question for printing.
        Hint: Return text + all options line by line.
        """
        display = f"\nQ{self.question_id}: {self.text}\n"
        for opt in self.options:
            display += f"  {opt}\n"
        return display
