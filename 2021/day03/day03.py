import os


class DiagnosticReport:
    def __init__(self, values):
        self.values = values

    def _find_common_bit_at_position(self, position):
        counts = {}

        for value in self.values:
            bit_value = value[position]
            if bit_value in counts.keys():
                counts[bit_value] += 1
            else:
                counts[bit_value] = 1
        return max(counts, key=counts.get)

    def _find_least_common_bit_at_position(self, position):
        counts = {}

        for value in self.values:
            bit_value = value[position]
            if bit_value in counts.keys():
                counts[bit_value] += 1
            else:
                counts[bit_value] = 1
        return min(counts, key=counts.get)

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
            epsilon_rate_binary_string += self._find_least_common_bit_at_position(
                bit_position
            )

        return bin2dec(epsilon_rate_binary_string)

    def calculate_power_consumption(self):
        return self.calculate_gamma_rate() * self.calculate_epsilon_rate()


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
