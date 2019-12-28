#!/usr/bin/env python3

input_init = 367479
input_end = 893698


# Rule 3 - at least two adjacent numbers are the same
def rule3(password):
    previous_char = None
    for char in password:
        if char == previous_char:
            return True
        previous_char = char
    return False


# Rule 3 (day 2) - has at least a set of at most two equal numbers adjacent to each other
#
# we only count number of occurrences as other rules ensure that if equal numbers show up they
# will be adjacent to each other
def rule3_day2(password):
    for char in password:
        if password.count(char) == 2:
            return True


# Rule 4 - from left to right, numbers never decrease (only increase or remain the same)
def rule4(password):
    previous_char = password[0]
    for char in password:
        if char < previous_char:
            return False
        previous_char = char
    return True


# Rule 1 - 6 digit number
# Rule 2 - within range
# Rule 3 - at least two adjacent numbers are the same
# Rule 3 day 2 - has a pair of adjacent equal numbers
# Rule 4 - from left to right, numbers never decrease (only increase or remain the same)
def check_valid(password):
    # rule 1
    if len(password) != 6:
        return False
    # rule 2
    if int(password) < input_init or int(password) > input_end:
        return False
    # rule4
    if not rule4(password):
        return False
    # rule 3 - runs after rule 4 as it uses it to eliminate invalid passwords and ensure the string is ordered correctly
    if not rule3_day2(password):
        return False
    return True


if __name__ == '__main__':
    valid = []
    for i in range(input_init, input_end + 1):
        if check_valid(str(i)):
            valid.append(i)
    print(valid)
    print(len(valid))
