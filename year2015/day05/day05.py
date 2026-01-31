import os

VOWELS = list("aeiou")


def three_vowels(string):
    # It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    vowel_counter = 0

    for letter in string:
        if letter in VOWELS:
            vowel_counter += 1

    return vowel_counter >= 3


def has_double(string):
    # It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    previous_letter = None

    for letter in string:
        if letter == previous_letter:
            return True
        previous_letter = letter

    return False


def rule_three(string):
    # It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    return not ("ab" in string or "cd" in string or "pq" in string or "xy" in string)


def is_nice(string):
    return three_vowels(string) and has_double(string) and rule_three(string)


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    nice_counter = 0

    with open(input_path) as input_file:
        for line in input_file:
            word_to_check = line.rstrip()
            if is_nice(word_to_check):
                nice_counter += 1

    print(nice_counter)
