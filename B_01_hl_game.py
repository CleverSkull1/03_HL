import random


# functions

def string_checker(question, valid_ans=('yes', 'no')):
    """Check that users have entered a valid response"""
    error = f"Please enter one of the following: " \
            f"{valid_ans}"

    while True:
        # get user response and make sure its lower case
        user_response = input(question).lower()

        for item in valid_ans:

            # check if the user response is a word in the list
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

            # print error if user enters invalid
        print(error)
        print()


def instructions():
    """Prints instructions"""

    make_statement("Instructions", "*")
    print("""
Choose the range in within which there wil be a random number

Try guess the number 
You will be told if your number is higher or lower than the correct one
    """)


def make_statement(statement, decoration):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def int_check(question):
    """Checks users enter an integer more than or equal to 1"""

    error = "Please enter an integer more than or equal to 1. "

    while True:
        try:
            response = int(input(question))

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def correct_answer_check(question):
    """Checks users enter an integer that is equal to the number"""

    error = "Please enter an integer more than or equal to 1. "

    while True:
        try:
            response = int(input(question))

            if response < random_num:
                print("Higher")
            elif response > random_num:
                print("Lower")
            else:
                print("\n🎉🎉🎉 Correct 🎉🎉🎉\n")

        except ValueError:
            print(error)


#  Main routine

print("\n📈📈📈 Higher or Lower 📉📉📉\n")

want_instructions = string_checker("Would you like to view the instructions? ").lower()

# Display the instructions if the user wants to see them.
if want_instructions == "yes":
    instructions()

print()

# choose random number
hl_range_1 = int_check("Choose the range for number 1: ")
hl_range_2 = int_check("Choose the range for number 2: ")
random_num = random.randint(hl_range_1, hl_range_2)


while True:
    correct_answer_check("Choose the number: ")
