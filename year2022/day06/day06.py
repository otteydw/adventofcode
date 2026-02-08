# mypy: ignore-errors
import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


def unique_chars_to_find(datastream, chars_to_find):
    for i in range(0, len(datastream) - chars_to_find - 1):
        signal_to_check = datastream[i : i + chars_to_find]
        unique = "".join(set(signal_to_check))

        if len(signal_to_check) == len(unique):
            return i + chars_to_find

    return -1


def start_of_packet(datastream):
    return unique_chars_to_find(datastream, 4)


def start_of_message(datastream):
    return unique_chars_to_find(datastream, 14)


if __name__ == "__main__":

    input_filename = "input.txt"

    datastream = load_from_file(input_filename)
    print(f"start-of-packet marker detected at: {start_of_packet(datastream[0])}")
    print(f"start-of-message marker detected at: {start_of_message(datastream[0])}")
