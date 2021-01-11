
# https://adventofcode.com/2020/day/1

inputs_path = 'input.txt'

with open(inputs_path) as inputs_file:
    entries = inputs_file.readlines()
entries = [int(x.strip()) for x in entries]

# print(entries)

for a in entries:
    for b in entries:
        if a + b == 2020:
            print(a * b)
            exit()
