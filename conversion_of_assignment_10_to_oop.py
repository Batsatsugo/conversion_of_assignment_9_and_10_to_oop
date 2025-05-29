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