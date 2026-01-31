import os


class DiagnosticReport:
    def __init__(self, values):
        self.values = values

    def _find_common_bit_at_position(self, position, values=None):
        if not values:
            values = self.values

        counts = {}

        for value in values:
            bit_value = value[position]
            if bit_value in counts.keys():
                counts[bit_value] += 1
            else:
                counts[bit_value] = 1

        if counts["1"] >= counts["0"]:
            return "1"
        else:
            return "0"

    def _find_least_common_bit_at_position(self, position, values=None):
        if not values:
            values = self.values

        counts = {}

        for value in values:
            bit_value = value[position]
            if bit_value in counts.keys():
                counts[bit_value] += 1
            else:
                counts[bit_value] = 1

        # Favor the 0s
        if counts["0"] <= counts["1"]:
            return "0"
        else:
            return "1"

    def calculate_gamma_rate(self):
        number_length = len(self.values[0])
        gamma_rate_binary_string = ""

        for bit_position in range(number_length):
            gamma_rate_binary_string += self._find_common_bit_at_position(bit_position)

        return bin2dec(gamma_rate_binary_string)

    def calculate_epsilon_rate(self):
        number_length = len(self.values[0])
        epsilon_rate_binary_string = ""

        for bit_position in range(number_length):
            epsilon_rate_binary_string += self._find_least_common_bit_at_position(bit_position)

        return bin2dec(epsilon_rate_binary_string)

    def calculate_power_consumption(self):
        return self.calculate_gamma_rate() * self.calculate_epsilon_rate()

    def calculate_life_support_rating(self):
        return self.calculate_oxygen_generator_rating() * self.calculate_CO2_scrubber_rating()

    def calculate_oxygen_generator_rating(self):
        return self._filter_by_bit_criteria("most")

    def calculate_CO2_scrubber_rating(self):
        return self._filter_by_bit_criteria("least")

    def _filter_by_bit_criteria(self, bit_criteria):
        number_length = len(self.values[0])
        remaining_values = self.values.copy()

        for bit_position in range(number_length):

            if bit_criteria == "most":
                value_to_match = self._find_common_bit_at_position(bit_position, remaining_values)
            elif bit_criteria == "least":
                value_to_match = self._find_least_common_bit_at_position(bit_position, remaining_values)
            else:
                raise Exception(f"Invalid bit_criteria {bit_criteria}!")

            new_remaining_values = []

            for value in remaining_values:
                if value[bit_position] == value_to_match:
                    new_remaining_values.append(value)

            if len(new_remaining_values) == 1:
                return bin2dec(new_remaining_values[0])
            else:
                remaining_values = new_remaining_values.copy()


def bin2dec(binary_value):
    return int(binary_value, 2)


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


if __name__ == "__main__":

    reported_values = load_from_file("input.txt")
    diag = DiagnosticReport(reported_values)

    print(f"Part 1 answer is: {diag.calculate_power_consumption()}")
    print(f"Part 2 answer is: {diag.calculate_life_support_rating()}")
