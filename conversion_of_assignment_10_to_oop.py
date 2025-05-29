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

    # method to load quiz questions from a file
    def load_questions(self):
        try:
            # try to open the quiz file in read mode
            with open(self.filename, "r") as file:
                lines = file.readlines()
                # loop through each line and parse it as JSON
                for i, line in enumerate(lines, 1):
                    try:
                        self.questions.append(json.loads(line))  # add valid question to list
                    except json.JSONDecodeError:
                        print(f"Skipping invalid question format on line {i}")  # handle bad data
            return True  # Indicate success
        except FileNotFoundError:
            # if the file doesn't exist, show an error message and exit
            print("❌ Quiz file not found! Please create the quiz first.")
            return False