# quiz_system.py
"""
QuizSystem class for managing quizzes and students.

Responsibilities:
- Store quizzes in dict {quiz_id: Quiz}
- Store students in dict {student_id: Student}
- Create quiz, add questions
- Register student
- Allow quiz attempt

💡 Hint:
- Use exceptions when invalid IDs are given
- When attempting quiz: call quiz.attempt() and record score in Student
"""
from quiz import Quiz
from student import Student
from exceptions import QuizNotFoundError, StudentNotFoundError

class QuizSystem:
    def __init__(self):
        # Initialize storage for quizzes and students
        self.quizzes = {}
        self.students = {}

    def create_quiz(self, quiz):
        """Add a new quiz to the system."""
        # Hint: self.quizzes[quiz.quiz_id] = quiz
        self.quizzes[quiz.quiz_id] = quiz

    def add_question_to_quiz(self, quiz_id, question):
        """Add a question to a quiz using its ID."""
        # Hint: Fetch quiz and call quiz.add_question()
        quiz = self.quizzes.get(quiz_id)
        if not quiz:
            raise QuizNotFoundError(f"Quiz '{quiz_id}' not found.")
        quiz.add_question(question)

    def register_student(self, student):
        """Register a new student."""
        # Hint: self.students[student.student_id] = student
        self.students[student.student_id] = student

    def attempt_quiz(self, student_id, quiz_id, answers_dict):
        """
        Attempt a quiz by a student.
        Hint: Get student + quiz, then update score.
        """
        quiz = self.quizzes.get(quiz_id)
        if not quiz:
            raise QuizNotFoundError(f"Quiz '{quiz_id}' not found.")
        student = self.students.get(student_id)
        if not student:
            raise StudentNotFoundError(f"Student '{student_id}' not found.")
        score = quiz.attempt(answers_dict)
        student.record_score(quiz_id, score)
        return score
