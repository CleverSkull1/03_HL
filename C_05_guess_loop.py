# fns

def make_statement(statement, decoration, amount):
    """Adds additional characters to the start and end of headings as decoration"""

    ends = decoration * amount
    print(f"\n{ends} {statement} {ends}")


def int_check(question, low=None, high=None, exit_code=None):
    """Checks users enter an integer more than or equal to 1"""

    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f"is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response
        try:
            response = int(response)
            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# variables

secret = 7
low_num = 0
high_num = 10
guesses_allowed = 5
guesses_used = 0
already_guessed = []
feedback = ""
guess = ""

# calcs
while guess != secret and guesses_used < guesses_allowed:
    # ask to guess
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # check for error code
    if guess == "xxx":
        end_game = "yes"
        break

    # check for dupes
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses ")
        continue

    # add valid guess to list
    else:
        already_guessed.append(guess)

    guesses_used += 1

    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, try higher "
                    f"You've used {guesses_used} / {guesses_allowed} guesses ")

    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, try lower "
                    f"You've used {guesses_used} / {guesses_allowed} guesses ")

    # when guessed correct
    elif guess == secret:
        if guesses_used == 1:
            feedback = "🍀🍀 Lucky! You were correct! 🍀🍀"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses "
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses "

    # if there are no remaining guesses
    else:
        feedback = "Sorry, you have run out of guesses. \n👎👎 You lose 👎👎"

    print(feedback)

    # additional feedback
    if guesses_used == guesses_allowed - 1:
        make_statement("Careful, you only have one guess left!", "💣", 2)

print("\nEnd of round")
