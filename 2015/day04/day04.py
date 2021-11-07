import hashlib
import os
import sys

def combine_secret_and_number(secret_key, number):
    return f"{secret_key}{number}"

def get_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def is_mineable(hash):
    return hash[:5] == "00000"

def find_answer(secret_key):

    counter = 0

    while True:
        str2hash = combine_secret_and_number(secret_key, counter)
        md5 = get_hash(str2hash)
        if is_mineable(md5):
            return counter
        counter += 1

if __name__ == "__main__":

    SECRET = "yzbqklnj"

    print(find_answer(SECRET))