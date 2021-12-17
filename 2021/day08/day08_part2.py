import os
from collections import defaultdict
import itertools


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
        # print(f"Appending {unique_signal_pattern} and {output_value}")
        unique_signal_patterns.append(unique_signal_pattern)
        output_values.append(output_value)

    return unique_signal_patterns, output_values


# def what_integer(value):

#     count_of_letters = defaultdict(int)
#     for letter in value:
#         count_of_letters[letter] += 1
#     unique_number_of_segments = len(count_of_letters)

#     if unique_number_of_segments == 2:
#         return 1
#     elif unique_number_of_segments == 4:
#         return 4
#     elif unique_number_of_segments == 3:
#         return 7
#     elif unique_number_of_segments == 7:
#         return 8
#     else:
#         return -1


# def count_digits(values_to_search, integers_to_match):

#     matching_count = 0

#     for value_to_search in itertools.chain.from_iterable(values_to_search):
#         this_integer = what_integer(value_to_search)
#         if this_integer in integers_to_match:
#             matching_count += 1

#     return matching_count

class ClockDecoder():
    def __init__(self, input_values):
        # print(input_values)
        self.input_values = set(input_values)
        self.mapping_value_to_integer = {}
        self.mapping_integer_to_value = {}
        self.mapping_segment = {}

        self.calibrate()

    # def what_integer(value):

    #     count_of_letters = defaultdict(int)
    #     for letter in value:
    #         count_of_letters[letter] += 1
    #     unique_number_of_segments = len(count_of_letters)

    #     if unique_number_of_segments == 2:
    #         return 1
    #     elif unique_number_of_segments == 4:
    #         return 4
    #     elif unique_number_of_segments == 3:
    #         return 7
    #     elif unique_number_of_segments == 7:
    #         return 8
    #     else:
    #         return -1
    # def set_top_segment(self):
    #     set_one = set(self.mapping_integer_to_value[1])
    #     set_seven = set(self.mapping_integer_to_value[7])

    #     self.mapping_segment['t'] = tuple(set_seven.difference(set_one))[0]

    # def set_bottom_left_segment(self):
    #     set_eight = set(self.mapping_integer_to_value[8])
    #     set_nine = set(self.mapping_integer_to_value[9])

    #     self.mapping_segment['bl'] = tuple(set_eight.difference(set_nine))[0]


    # def set_unique_mappings(self):
    #     # 1, 4, 7, 8
    #     for value in self.input_values:
    #         this_integer = what_integer(value)
    #         if this_integer in [1, 4, 7, 8]:
    #             self.mapping_value_to_integer[value] = this_integer
    #             self.mapping_integer_to_value[this_integer] = value

    # def set_nine_and_bottom_segment(self):
    #     for value in self.input_values:
    #         if len(value) == 6:
    #             if set(self.mapping_integer_to_value[4]).issubset(set(value)):
    #                 self.mapping_value_to_integer[value] = 9
    #                 self.mapping_integer_to_value[9] = value
    #             elif set(self.mapping_integer_to_value[1]).issubset(set(value)):
    #                 self.mapping_value_to_integer[value] = 0
    #                 self.mapping_integer_to_value[0] = value
    #             else:
    #                 self.mapping_value_to_integer[value] = 6
    #                 self.mapping_integer_to_value[6] = value

        # for value in self.input_values:
        #     if len(value) == 5:
        #         if not set(set(value)).issubset(self.mapping_integer_to_value[9]):
        #             self.mapping_value_to_integer[value] = 2
        #             self.mapping_integer_to_value[2] = value
        #         elif set(set(value)).issubset(self.mapping_integer_to_value[6]):
        #             self.mapping_value_to_integer[value] = 5
        #             self.mapping_integer_to_value[5] = value
        #         else:
        #             self.mapping_value_to_integer[value] = 3
        #             self.mapping_integer_to_value[3] = value


    def calibrate(self):

        # 1, 4, 7, 8
        # for value in self.input_values:
        #     this_integer = what_integer(value)
        #     if this_integer in [1, 4, 7, 8]:
        #         self.mapping_value_to_integer[value] = this_integer
        #         self.mapping_integer_to_value[this_integer] = value

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
        # self.set_unique_mappings()

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
        # self.set_nine_and_bottom_segment()
        #HAVE: 1, 4, 7, 8, 9
        #LEFT: 0, 2, 3, 5, 6

        # self.set_bottom_left_segment()
        # self.set_bottom_segment()

        # self.zero_or_six()

    def map_val_to_int(self):
        return self.mapping_value_to_integer

    def map_int_to_val(self):
        return self.mapping_integer_to_value

    def map_segment(self):
        return self.mapping_segment

    def decode_list(self, values):
        return_string=""
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

    # _, output_values = parse_input("input.txt")
    # print(f"Part 1: {count_digits(output_values, [1,4,7,8])}")

    # input_values, output_values = parse_input("example1.txt")
    # # print(input_values)
    # # print(output_values)
    # for input_value, output_value in zip(input_values, output_values):
    #     mycode = ClockDecoder(input_value)

    #     print(mycode.map_int_to_val())
    #     print(mycode.map_val_to_int())
    #     print(mycode.map_segment())
    #     print(mycode.decode_list(output_value))
    # print(calibrate(input_values[0]))

    print(f"Part 2: {sum_decoded_values_from_input('input.txt')}")