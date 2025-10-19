# main.py
"""
Main entry point for Online Quiz System.

Instructions:
1. Import QuizSystem class from quiz_system.py
2. Create an instance of QuizSystem
3. Provide a menu with options:
   - Create Quiz
   - Add Question to Quiz
   - Register Student
   - Attempt Quiz
   - View Reports
   - Exit
4. Use input() to capture user actions and call QuizSystem methods.

💡 Hint:
- Wrap risky operations in try/except (invalid quiz ID, wrong student ID).
"""
from utils import generate_id
from quiz_system import QuizSystem
from quiz import Quiz
from question import Question
from student import Student
from exceptions import QuizNotFoundError, StudentNotFoundError
from report import quiz_report, student_report

def main():
    quiz_system = QuizSystem()

    while True:
        print("\n=== k Online Quiz System ===")
        print("1. Create Quiz")
        print("2. Add Question to Quiz")
        print("3. Register Student")
        print("4. Attempt Quiz")
        print("5. View Reports")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            title = input("Enter quiz title: ")
            quiz_id = generate_id("QUIZ")
            quiz = Quiz(quiz_id, title)
            quiz_system.create_quiz(quiz)
            print(f" Quiz '{title}' created with ID: {quiz_id}")

        elif choice == "2":
            quiz_id = input("Enter quiz ID: ")
            try:
                qid = generate_id("QUES")
                text = input("Enter question text: ")
                options = []
                for opt in ["A", "B", "C", "D"]:
                    options.append(f"{opt}. {input(f'Enter option {opt}: ')}")
                correct = input("Enter correct option (A/B/C/D): ").strip().upper()
                question = Question(qid, text, options, correct)
                quiz_system.add_question_to_quiz(quiz_id, question)
                print(" Question added successfully.")
            except QuizNotFoundError as e:
                print(f" {e}")

        elif choice == "3":
            name = input("Enter student name: ")
            sid = generate_id("STUD")
            student = Student(sid, name)
            quiz_system.register_student(student)
            print(f" Student '{name}' registered with ID: {sid}")

        elif choice == "4":
            sid = input("Enter student ID: ")
            qid = input("Enter quiz ID: ")
            try:
                quiz = quiz_system.quizzes[qid]
                print(f"\nStarting Quiz: {quiz.title}")
                answers = {}
                for q in quiz.questions:
                    print(q)
                    ans = input("Your answer (A/B/C/D): ").strip().upper()
                    answers[q.question_id] = ans
                score = quiz_system.attempt_quiz(sid, qid, answers)
                print(f" Your Score: {score}/{len(quiz.questions)}")
            except (QuizNotFoundError, StudentNotFoundError) as e:
                print(f" {e}")

        elif choice == "5":
            print("\n1. Quiz Report")
            print("2. Student Report")
            sub = input("Enter choice: ")
            if sub == "1":
                qid = input("Enter quiz ID: ")
                if qid in quiz_system.quizzes:
                    quiz_report(quiz_system.quizzes[qid])
                else:
                    print(" Quiz not found.")
            elif sub == "2":
                sid = input("Enter student ID: ")
                if sid in quiz_system.students:
                    student_report(quiz_system.students[sid])
                else:
                    print(" Student not found.")

        elif choice == "6":
            print(" Exiting Quiz System. Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
