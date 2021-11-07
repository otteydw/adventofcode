import hashlib
import os
import sys

def combine_secret_and_number(secret_key, number):
    return f"{secret_key}{number}"

def get_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def is_mineable(hash, num_zeroes=5):
    return hash[:num_zeroes] == "0" * num_zeroes

def find_answer(secret_key, num_zeroes=5):

    counter = 0

    while True:
        str2hash = combine_secret_and_number(secret_key, counter)
        md5 = get_hash(str2hash)
        if is_mineable(md5, num_zeroes):
            return counter
        counter += 1

if __name__ == "__main__":

    SECRET = "yzbqklnj"

    print(f"5 zeroes: {find_answer(SECRET)}")
    print(f"6 zeroes: {find_answer(SECRET, 6)}")