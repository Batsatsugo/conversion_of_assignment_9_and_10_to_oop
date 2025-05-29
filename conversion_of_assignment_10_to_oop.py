import json

# define a class to encapsulate all functionality related to running the quiz
class QuizGame:
    # constructor method to initialize the filename and prepare score and question list
    def __init__(self, filename="the_ultimate_quiz_data.txt"):
        self.filename = filename    # File where quiz questions are stored
        self.score = 0              # Initialize score to 0
        self.questions = []         # List to store all loaded quiz questions

    # method to start the quiz
    def start(self):
        print("\n🧠 Welcome to The Ultimate Quiz Game! 🧠\n")

        # attempt to load quiz questions
        if not self.load_questions():
            return                  # exit if questions couldn't be loaded

        total = len(self.questions)

        # Loop through each question with its number
        for i, question_data in enumerate(self.questions, 1):
            self.ask_question(i, question_data)

        print(f"\n🎉 Quiz completed! You scored {self.score}/{total}.")