# mypy: ignore-errors
import copy
import os


class Circuit:
    def __init__(self):
        self.gate = dict()
        self.bit_mask = 0xFFFF  # bit_mask reference thanks to https://github.com/jdswalker/Advent-of-Code-2015/blob/2e9a1e1441db92eee318c9ddb357f4e4b1f2f76c/advent_of_code/solvers/day_07.py#L221

    def __str__(self):
        return str(self.gate)

    def get_signal(self, wire):

        # If the input "wire" is actually a number, just return that number directly.
        if wire.isnumeric():
            return int(wire)

        # If the wire has an integer value, return that.
        value = self.gate[wire]
        if isinstance(value, int):
            return value

        # Otherwise this wire is storing a direction, so we will process that.
        # then store the returned (integer) value onto the wire to reduce future recursion.
        return_value = self.get_signal_from_direction(value)
        self.set_signal(wire, return_value)
        return return_value

    def get_signal_from_direction(self, direction):
        # print(f"Parsing direction: {direction}")
        if "AND" in direction:
            # x AND y
            wire_a, wire_b = direction.split(" AND ")
            value_a = self.get_signal(wire_a)
            value_b = self.get_signal(wire_b)
            value = (value_a & value_b) & self.bit_mask
            return value
        elif "OR" in direction:
            # x OR y
            wire_a, wire_b = direction.split(" OR ")
            value_a = self.get_signal(wire_a)
            value_b = self.get_signal(wire_b)
            value = (value_a | value_b) & self.bit_mask
            return value

        elif "LSHIFT" in direction:
            # x LSHIFT 2
            wire_a, shift_distance = direction.split(" LSHIFT ")
            value_a = self.get_signal(wire_a)
            value = (value_a << int(shift_distance)) & self.bit_mask
            return value

        elif "RSHIFT" in direction:
            # y RSHIFT 2
            wire_a, shift_distance = direction.split(" RSHIFT ")
            value_a = self.get_signal(wire_a)
            value = (value_a >> int(shift_distance)) & self.bit_mask
            return value

        elif "NOT" in direction:
            # NOT x
            wire_a = direction.strip("NOT ")
            value_a = self.get_signal(wire_a)
            value = ~value_a & self.bit_mask
            return value
        else:
            wire_a = direction
            return self.get_signal(wire_a)

    def set_signal(self, wire, value):
        if isinstance(value, str) and value.isnumeric():
            value = int(value)
        self.gate[wire] = value

    def store_direction(self, direction):
        operation, wire = direction.split(" -> ")
        self.set_signal(wire, operation)


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    circuit = Circuit()

    with open(input_path) as input_file:
        for index, line in enumerate(input_file):
            this_direction = line.rstrip()
            circuit.store_direction(this_direction)

    # Backup the circuit before processing any inputs
    circuit_backup = copy.deepcopy(circuit)

    first_run_a = circuit.get_signal("a")
    print(f"Value of a: {first_run_a}")

    # Reset the circuit from backup
    circuit = copy.deepcopy(circuit_backup)

    # Override b with the value of a from the first run
    circuit.store_direction(f"{first_run_a} -> b")

    second_run_a = circuit.get_signal("a")
    print(f"Value of a: {second_run_a}")
