import math


# calculate the number of guesses allowed

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)


to_test = [
    (1, 10, 5),
    (1, 20, 6),
    (1, 100, 8),
    (1, 100, 11),
]

# run tests
for item in to_test:
    low_num = item[0]
    high_num = item[1]
    expected = item[2]

    actual = calc_guesses(low_num, high_num)
    if actual == expected:
        print(f"Passed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual}")
    else:
        print(f"Passed! Case: {low_num}-{high_num}, expected: {expected}, received: {actual}")
