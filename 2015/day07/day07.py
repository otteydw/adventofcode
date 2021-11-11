import os
import sys


class Circuit:
    def __init__(self):
        self.gate = dict()
        self.bit_mask = 0xFFFF # bit_mask reference thanks to https://github.com/jdswalker/Advent-of-Code-2015/blob/2e9a1e1441db92eee318c9ddb357f4e4b1f2f76c/advent_of_code/solvers/day_07.py#L221

    def __str__(self):
        return str(self.gate)

    def get_signal(self, wire):
        if wire.isnumeric():
            return int(wire)
        value = self.gate[wire]
        if isinstance(value, int):
            return value
        else:
            return(self.get_signal_from_direction(value))

    def get_signal_from_direction(self, direction):
        print(f"Parsing direction: {direction}")
        if "AND" in direction:
            # x AND y
            wire_a, wire_b = direction.split(' AND ')
            value_a = self.get_signal(wire_a)
            value_b = self.get_signal(wire_b)
            value = (value_a & value_b) & self.bit_mask
            return value
        elif "OR" in direction:
            # x OR y
            wire_a, wire_b = direction.split(' OR ')
            value_a = self.get_signal(wire_a)
            value_b = self.get_signal(wire_b)
            value = (value_a | value_b) & self.bit_mask
            return value

        elif "LSHIFT" in direction:
            # x LSHIFT 2
            wire_a, shift_distance = direction.split(' LSHIFT ')
            value_a = self.get_signal(wire_a)
            value = (value_a << int(shift_distance)) & self.bit_mask
            return value

        elif "RSHIFT" in direction:
            # y RSHIFT 2
            wire_a, shift_distance = direction.split(' RSHIFT ')
            value_a = self.get_signal(wire_a)
            value = (value_a >> int(shift_distance)) & self.bit_mask
            return value

        elif "NOT" in direction:
            # NOT x
            wire_a = direction.strip('NOT ')
            value_a = self.get_signal(wire_a)
            value = ~ value_a & self.bit_mask
            return value
        else:
            wire_a = direction
            return self.get_signal(wire_a)

    def set_signal(self, wire, value):
        if isinstance(value, str) and value.isnumeric():
            value = int(value)
        self.gate[wire] = value

    def store_direction(self, direction):
        operation, wire = direction.split(' -> ')
        self.set_signal(wire, operation)





    # def parse_and_or(self, direction, verb):
    #     # Common parser for AND, OR
    #     operation, wire = direction.split(' -> ')
    #     wire_a, wire_b = operation.split(f' {verb} ')
    #     value_a = self.get_signal(wire_a)
    #     value_b = self.get_signal(wire_b)

    #     return wire, value_a, value_b

    # def parse_shift(self, direction, verb):
    #     # Common parser for LSHIFT and RSHIFT
    #     operation, wire = direction.split(' -> ')
    #     wire_a, shift_distance = operation.split(f' {verb} ')
    #     value_a = self.get_signal(wire_a)

    #     return wire, value_a, int(shift_distance)

    # def go(self, direction):

    #     bit_mask = 0xFFFF

    #     if "AND" in direction:
    #         # x AND y -> d
    #         wire, value_a, value_b = self.parse_and_or(direction, 'AND')
    #         value = (value_a & value_b) & bit_mask
    #         self.set_signal(wire, value)
    #     elif "OR" in direction:
    #         # x OR y -> d
    #         wire, value_a, value_b = self.parse_and_or(direction, 'OR')
    #         value = (value_a | value_b) & bit_mask
    #         self.set_signal(wire, value)
    #     elif "LSHIFT" in direction:
    #         # x LSHIFT 2 -> f
    #         wire, value_a, shift_distance = self.parse_shift(direction, 'LSHIFT')
    #         value = (value_a << shift_distance) & bit_mask
    #         self.set_signal(wire, value)
    #     elif "RSHIFT" in direction:
    #         # y RSHIFT 2 -> g
    #         wire, value_a, shift_distance = self.parse_shift(direction, 'RSHIFT')
    #         value = (value_a >> shift_distance) & bit_mask
    #         self.set_signal(wire, value)
    #     elif "NOT" in direction:
    #         # NOT x -> h
    #         operation = direction.split()
    #         wire_a, wire_b = operation[1], operation[3]
    #         value_a = self.get_signal(wire_a)
    #         value = ~ value_a & bit_mask
    #         # value = 65535 - self.get_signal(wire_a)
    #         self.set_signal(wire_b, value)
    #     else:
    #         # assignment
    #         # 123 -> x
    #         value, wire = direction.split(' -> ')
    #         self.set_signal(wire, value)


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    circuit = Circuit()

    with open(input_path) as input_file:
        for index, line in enumerate(input_file):
            this_direction = line.rstrip()
            # print(index, this_direction)
            # circuit.go(this_direction)
            circuit.store_direction(this_direction)

    circuit.get_signal('a')
    # print(circuit)