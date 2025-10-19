# report.py
"""
Reporting functions for quizzes and students.

Functions:
- quiz_report(quiz)
- student_report(student)

💡 Hint:
- quiz_report → print quiz title and number of questions.
- student_report → print student name and quiz_scores.
"""

def quiz_report(quiz):
    """Generate a report for a specific quiz."""
    print(f"\n📘 Quiz Report: {quiz.title}")
    print(f"Total Questions: {len(quiz.questions)}")
    for q in quiz.questions:
        print(q)

def student_report(student):
    """Generate a report for a specific student."""
    print(f"\n👩‍🎓 Student Report: {student.name}")
    if not student.quiz_scores:
        print("No quizzes attempted yet.")
    else:
        for quiz_id, score in student.quiz_scores.items():
            print(f"Quiz ID: {quiz_id} | Score: {score}")
