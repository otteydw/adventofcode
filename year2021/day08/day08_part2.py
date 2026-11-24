# mypy: ignore-errors
import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def sort_string(string):
    return "".join(sorted(string))


def parse_input(filename, sort_output=True):

    input_strings = load_from_file(filename)

    unique_signal_patterns = []
    output_values = []

    for line in input_strings:
        unique_signal_pattern_string, output_value_string = line.split(" | ")
        unique_signal_pattern = unique_signal_pattern_string.split()
        output_value = output_value_string.split()

        if sort_output:
            unique_signal_pattern = [sort_string(x) for x in unique_signal_pattern]
            output_value = [sort_string(x) for x in output_value]
        unique_signal_patterns.append(unique_signal_pattern)
        output_values.append(output_value)

    return unique_signal_patterns, output_values


class ClockDecoder:
    def __init__(self, input_values):

        self.input_values = set(input_values)
        self.mapping_value_to_integer = {}
        self.mapping_integer_to_value = {}
        self.mapping_segment = {}

        self.calibrate()

    def calibrate(self):

        # 1, 4, 7, 8
        for value in self.input_values:
            if len(value) == 2:
                self.mapping_value_to_integer[value] = 1
                self.mapping_integer_to_value[1] = value
            elif len(value) == 4:
                self.mapping_value_to_integer[value] = 4
                self.mapping_integer_to_value[4] = value
            elif len(value) == 3:
                self.mapping_value_to_integer[value] = 7
                self.mapping_integer_to_value[7] = value
            elif len(value) == 7:
                self.mapping_value_to_integer[value] = 8
                self.mapping_integer_to_value[8] = value

        # 0, 6, 9
        for value in self.input_values:
            if len(value) == 6:
                if set(self.mapping_integer_to_value[4]).issubset(set(value)):
                    self.mapping_value_to_integer[value] = 9
                    self.mapping_integer_to_value[9] = value
                elif set(self.mapping_integer_to_value[1]).issubset(set(value)):
                    self.mapping_value_to_integer[value] = 0
                    self.mapping_integer_to_value[0] = value
                else:
                    self.mapping_value_to_integer[value] = 6
                    self.mapping_integer_to_value[6] = value

        # 2, 3, 5
        for value in self.input_values:
            if len(value) == 5:
                if not set(set(value)).issubset(self.mapping_integer_to_value[9]):
                    self.mapping_value_to_integer[value] = 2
                    self.mapping_integer_to_value[2] = value
                elif set(set(value)).issubset(self.mapping_integer_to_value[6]):
                    self.mapping_value_to_integer[value] = 5
                    self.mapping_integer_to_value[5] = value
                else:
                    self.mapping_value_to_integer[value] = 3
                    self.mapping_integer_to_value[3] = value

    def map_val_to_int(self):
        return self.mapping_value_to_integer

    def map_int_to_val(self):
        return self.mapping_integer_to_value

    def map_segment(self):
        return self.mapping_segment

    def decode_list(self, values):
        return_string = ""
        for value in values:
            return_string += str(self.decode_string(value))

        return return_string

    def decode_string(self, value):
        sorted_value = "".join(sorted(value))
        return self.mapping_value_to_integer[sorted_value]


def sum_decoded_values_from_input(filename):
    sum = 0
    input_values, output_values = parse_input(filename)
    for input_value, output_value in zip(input_values, output_values):
        mycode = ClockDecoder(input_value)
        sum += int(mycode.decode_list(output_value))

    return sum


if __name__ == "__main__":

    print(f"Part 2: {sum_decoded_values_from_input('input.txt')}")
