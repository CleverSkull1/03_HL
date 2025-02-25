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


# main routine starts here