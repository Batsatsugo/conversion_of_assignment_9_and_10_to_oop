import json

# define a class to encapsulate the quiz creation functionality
class QuizCreator:
    # defining and initializing filename to save the quiz data
    def __init__(self, filename="the_ultimate_quiz_data.txt"):
        self.filename = filename

    # main method to run the quiz creator interface
    def run(self):
        print("\n🔥 Welcome to the Ultimate Quiz Creator! 🔥\n")
        