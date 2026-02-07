import os

VOWELS = list("aeiou")


def rule1(string):
    """
    It contains a pair of any two letters that appears at least twice in the string without overlapping,
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    """
    if len(string) < 4:
        return False

    for index in range(len(string)):
        current_pair = string[index : index + 2]
        remainder_of_string = string[index + 2 :]
        if current_pair in remainder_of_string:
            return True
    return False


def rule2(string):
    """
    It contains at least one letter which repeats with exactly one letter between them,
    like xyx, abcdefeghi (efe), or even aaa.
    """

    if len(string) < 3:
        return False

    for index, letter in enumerate(string[2:]):
        if string[index] == letter:
            return True

    return False


def is_nice(string):
    return rule1(string) and rule2(string)


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    nice_counter = 0

    with open(input_path) as input_file:
        for line in input_file:
            word_to_check = line.rstrip()
            if is_nice(word_to_check):
                nice_counter += 1

    print(nice_counter)
