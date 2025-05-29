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

                # ask user if they want to add another question
                another = input("\nDo you want to add another question? (yes/no): ").strip().lower()
                # if user does not type 'yes', break the loop and end
                if another != "yes":
                    print(f"\n✅ All questions have been saved to '{self.filename}'. ✅")
                    break

    def create_question(self):
        # prompt user to enter the question text
        question_text = input("\nEnter your question: ")
        # initialize an empty dictionary to store multiple-choice options
        choices = {}

        # loop through choice labels a–d to collect each option from the user
        for option in ['a', 'b', 'c', 'd']:
            choices[option] = input(f"Enter choice {option.upper()}: ")

        # prompt user to enter the correct answer and must be a, b, c, d
        correct_answer = input("Enter the correct answer (a, b, c, or d): ").lower()
        while correct_answer not in choices:
            print("Invalid choice. Please enter a valid option (a, b, c, or d).")
            correct_answer = input("Enter the correct answer: ").lower()

        # return the structured question data as a dictionary
        return {
            "question": question_text,
            "choices": choices,
            "answer": correct_answer
        }