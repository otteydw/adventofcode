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

def check_two_adjacent_same(password):
    """ For a given input, return true if two adjacent digits are equal """
    strPassword=str(password)
    for i in range(0, len(strPassword)-1):
        if strPassword[i] == strPassword[i+1]:
            return True
    return False


# print(check_two_adjacent_same(111111))  # True
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
