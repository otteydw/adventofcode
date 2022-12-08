import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


def start_of_packet(datastream):
    for i in range(0, len(datastream) - 3):
        signal_to_check = datastream[i : i + 4]
        unique = "".join(set(signal_to_check))

        if len(signal_to_check) == len(unique):
            return i + 4

    return -1


if __name__ == "__main__":

    input_filename = "input.txt"

    data = load_from_file(input_filename)
    print(f"start-of-packet marker detected at: {start_of_packet(data[0])}")
