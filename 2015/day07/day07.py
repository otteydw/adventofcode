import os
import sys


class Circuit:
    def __init__(self):
        self.gate = dict()

    def get_signal(self, wire):
        return int(self.gate[wire])

    def set_signal(self, wire, value):
        self.gate[wire] = int(value)

    def parse_and_or(self, direction, verb):
        # Common parser for AND, OR
        operation, wire = direction.split(' -> ')
        wire_a, wire_b = operation.split(f' {verb} ')
        value_a = self.get_signal(wire_a)
        value_b = self.get_signal(wire_b)

        return wire, value_a, value_b

    def parse_shift(self, direction, verb):
        # Common parser for LSHIFT and RSHIFT
        operation, wire = direction.split(' -> ')
        wire_a, shift_distance = operation.split(f' {verb} ')
        value_a = self.get_signal(wire_a)

        return wire, value_a, int(shift_distance)

    def go(self, direction):
        # bit_mask reference thanks to https://github.com/jdswalker/Advent-of-Code-2015/blob/2e9a1e1441db92eee318c9ddb357f4e4b1f2f76c/advent_of_code/solvers/day_07.py#L221
        bit_mask = 0xFFFF

        if "AND" in direction:
            # x AND y -> d
            wire, value_a, value_b = self.parse_and_or(direction, 'AND')
            value = (value_a & value_b) & bit_mask
            self.set_signal(wire, value)
        elif "OR" in direction:
            # x OR y -> d
            wire, value_a, value_b = self.parse_and_or(direction, 'OR')
            value = (value_a | value_b) & bit_mask
            self.set_signal(wire, value)
        elif "LSHIFT" in direction:
            # x LSHIFT 2 -> f
            wire, value_a, shift_distance = self.parse_shift(direction, 'LSHIFT')
            value = (value_a << shift_distance) & bit_mask
            self.set_signal(wire, value)
        elif "RSHIFT" in direction:
            # y RSHIFT 2 -> g
            wire, value_a, shift_distance = self.parse_shift(direction, 'RSHIFT')
            value = (value_a >> shift_distance) & bit_mask
            self.set_signal(wire, value)
        elif "NOT" in direction:
            # NOT x -> h
            operation = direction.split()
            wire_a, wire_b = operation[1], operation[3]
            value_a = self.get_signal(wire_a)
            value = ~ value_a & bit_mask
            # value = 65535 - self.get_signal(wire_a)
            self.set_signal(wire_b, value)
        else:
            # assignment
            # 123 -> x
            value, wire = direction.split(' -> ')
            self.set_signal(wire, value)


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    circuit = Circuit()

    with open(input_path) as input_file:
        for index, line in enumerate(input_file):
            this_direction = line.rstrip()
            print(index, this_direction)
            circuit.go(this_direction)

    circuit.get_signal('a')