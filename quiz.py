# quiz.py
"""
Quiz class to manage a collection of questions.

Attributes:
- quiz_id (str)
- title (str)
- questions (list of Question objects)

Methods:
- add_question(question)
- attempt(answers_dict) → returns score
- __str__() → print quiz summary

💡 Hint:
- Store questions in a list.
- In attempt(), loop through questions and check answers.
"""
from question import Question

class Quiz:
    def __init__(self, quiz_id, title):
        # Initialize quiz with ID, title, and empty question list
        self.quiz_id = quiz_id
        self.title = title
        self.questions = []

    def add_question(self, question):
        """Add a Question object to the quiz."""
        # Hint: self.questions.append(question)
        self.questions.append(question)

    def attempt(self, answers_dict):
        """
        answers_dict → {question_id: student_answer}
        Hint: Loop through self.questions and check answers.
        Return score as number of correct answers.
        """
        score = 0
        for q in self.questions:
            ans = answers_dict.get(q.question_id)
            if ans and q.check_answer(ans):
                score += 1
        return score

    def __str__(self):
        """Hint: Return quiz_id, title, and number of questions."""
        return f"Quiz [{self.quiz_id}] - {self.title} ({len(self.questions)} questions)"
