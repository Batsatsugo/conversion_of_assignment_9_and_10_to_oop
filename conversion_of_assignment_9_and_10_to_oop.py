import json

# define a class to encapsulate the quiz creation functionality
class QuizCreator:
    # defining and initializing filename to save the quiz data
    def __init__(self, filename="the_ultimate_quiz_data.txt"):
        self.filename = filename

    def run(self):