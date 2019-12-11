#!/usr/bin/python3

# https://adventofcode.com/2019/day/4

# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 193651-649729.

# --- Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

# Given this additional criterion, but still ignoring the range rule, the following are now true:

# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

# How many different passwords within the range given in your puzzle input meet all of the criteria?

def check_two_adjacent_same(password):
    """ For a given input, return true if two adjacent digits are equal AND the two adjacent matching digits are not part of a larger group of matching digits """
    strPassword=str(password)
    count_doubles=0 # Count the number of times two digits are the same
    count_triples=0 # Count the number of times three digits are the same
    for i in range(0, len(strPassword)-1):
        if strPassword[i] == strPassword[i+1]:
            return True
    return False


# print(check_two_adjacent_same(111111))  # False
# print(check_two_adjacent_same(101010))  # False
# print(check_two_adjacent_same(123455))  # True

def check_digits_decrease(password):
    """ For a given input, return true if the digits decrease from left ro right """
    strPassword=str(password)
    for i in range(0, len(strPassword)-1):
        if strPassword[i] > strPassword[i+1]:
            return True
    return False

# print(check_digits_decrease(111111))  # False
# print(check_digits_decrease(101010))  # True
# print(check_digits_decrease(123455))  # False

def generate_non_decreasing_integer(rangeStart, rangeStop):
    """ Create a set of numbers where the digits never decrease """
    for a in range(0,10):
        for b in range(a,10):
            for c in range(b,10):
                for d in range(c,10):
                    for e in range(d,10):
                        for f in range(e,10):
                            myInteger = int((str(str(a) + str(b) + str(c) + str(d) + str(e) + str(f))))
                            if rangeStart <= myInteger <= rangeStop:
                                yield myInteger

myRangeStart=193651
myRangeStop=649729



# exit()

counter=0
# for myPass in range(myRangeStart, myRangeStop):
for myPass in generate_non_decreasing_integer(myRangeStart, myRangeStop):
    # print(myPass)
    if check_two_adjacent_same(myPass) and not check_digits_decrease(myPass):
        counter+=1

print(counter)