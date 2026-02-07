import hashlib


def combine_secret_and_number(secret_key: str, number: int) -> str:
    return f"{secret_key}{number}"


def get_hash(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def is_mineable(hash: str, num_zeroes: int = 5) -> bool:
    return hash[:num_zeroes] == "0" * num_zeroes


def find_answer(secret_key: str, num_zeroes: int = 5) -> int:
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
