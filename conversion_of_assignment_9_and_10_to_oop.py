import json

# define a class to encapsulate the quiz creation functionality
class QuizCreator:
    # defining and initializing filename to save the quiz data
    def __init__(self, filename="the_ultimate_quiz_data.txt"):
        self.filename = filename

    # main method to run the quiz creator interface
    def run(self):
        print("\n🔥 Welcome to the Ultimate Quiz Creator! 🔥\n")

        # open the file in append mode to save questions
        with open(self.filename, "a") as file:
            # loop to allow multiple questions to be added
            while True:
                question_data = self.create_question()
                # convert the question dictionary to a JSON string and write to file
                file.write(json.dumps(question_data) + "\n")