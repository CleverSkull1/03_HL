# functions

def make_statement(statement, decoration):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")


def string_checker(question, valid_ans=('yes', 'no')):
    """Check that users have entered a valid option based on a list"""
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


def int_check(question):
    """Checks users enter an integer more than or equal to 1"""
    while True:
        error = "Please enter an integer more than or equal to 13. "

        to_check = input(question)

        # check for inf mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    """Prints instructions"""

    make_statement("Instructions", "*")
    print("""
Rock > Scissors
Scissors > Paper
Paper > Rock
    """)


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

print("\n📈📈📈 Higher or Lower 📉📉📉\n")

# instructions
want_instructions = string_checker("Would you like to view the instructions? ").lower()

# Display the instructions if the user wants to see them.
if want_instructions == "yes":
    instructions()

print()

# choose number of rounds
num_rounds = int_check("How many rounds would you like? Press <enter> for infinite ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop
while rounds_played < num_rounds:

    # round heading
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🪨📃✂️ Round {rounds_played + 1} of {num_rounds} ✂️📃🪨"

    print(rounds_heading, "\n")

    user_choice = input("Choose: ")

    # exit code
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in inf mode increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends

# game stats
