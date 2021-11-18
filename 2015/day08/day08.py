import os
import re
import sys

class SantaList:
    def __init__(self):
        self.memory_chars = 0
        self.string_literal_chars = 0
        self.memory_escaped = 0

    def _count_string_literal_chars(self, string):
        stripped_string = string[1:-1]
        string_literal_chars = bytes(stripped_string, 'utf-8').decode('unicode-escape')
        return len(string_literal_chars)

    def _count_memory_chars(self, string):
        return len(string)

    def _count_memory_escaped(self, string):
        # Some logic from https://github.com/jjhelmus/adventofcode/blob/master/day08.py
        string = string.replace("\\", "\\\\")
        escaped = string.replace('"', '\\"')
        escaped = f'"{escaped}"'
        return(len(escaped))

    def add(self, string):
        self.memory_chars += self._count_memory_chars(string)
        self.string_literal_chars += self._count_string_literal_chars(string)
        self.memory_escaped += self._count_memory_escaped(string)

    def get_memory_chars(self):
        return self.memory_chars

    def get_string_literal_chars(self):
        return self.string_literal_chars

    def get_memory_escaped(self):
        return self.memory_escaped

if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    santa_list = SantaList()

    with open(input_path) as input_file:
        for index, line in enumerate(input_file):
            this_line = line.rstrip()
            # print(this_line)
            santa_list.add(this_line)

    # print(santa_list.get_memory_chars())
    # print(santa_list.get_string_literal_chars())
    print(santa_list.get_memory_chars() - santa_list.get_string_literal_chars())
    print(santa_list.get_memory_escaped() - santa_list.get_memory_chars())