#!/usr/bin/python3

# https://adventofcode.com/2019/day/3

# --- Day 3: Crossed Wires ---
# The gravity assist was successful, and you're well on your way to the Venus
# refuelling station. During the rush back on Earth, the fuel management system
# wasn't completely installed, so that's next on the priority list.

# Opening the front panel reveals a jumble of wires. Specifically, two wires are
# connected to a central port and extend outward on a grid. You trace the path
# each wire takes as it leaves the central port, one wire per line of text (your
# puzzle input).

# The wires twist and turn, but the two wires occasionally cross paths. To fix
# the circuit, you need to find the intersection point closest to the central
# port. Because the wires are on a grid, use the Manhattan distance for this
# measurement. While the wires do technically cross right at the central port
# where they both start, this point does not count, nor does a wire count as
# crossing with itself.

## A taxicab geometry is a form of geometry in which the usual distance function
## or metric of Euclidean geometry is replaced by a new metric in which the
## distance between two points is the sum of the absolute differences of their
## Cartesian coordinates.

# For example, if the first wire's path is R8,U5,L5,D3, then starting from the
# central port (o), it goes right 8, up 5, left 5, and finally down 3:

# ...........
# ...........
# ...........
# ....+----+.
# ....|....|.
# ....|....|.
# ....|....|.
# .........|.
# .o-------+.
# ...........
# Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
# These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

# Here are a few more examples:

# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

# What is the Manhattan distance from the central port to the closest intersection?

class Wire():

    def __init__(self):
        self.coordinates = [0, 0]   # Use a list because tuples cannot be modified.
        self.history = set()        # Use a set because we do not care about duplicates, and sets are much faster to parse than lists.

    def alter_path(self, path):
        # Take a sequence of comma-separated requests and process them one at a time
        SEQUENCE = path.rstrip().split(',')

        for count, request in enumerate(SEQUENCE):
            print(str(count) + '/' + str(len(SEQUENCE)) + ' = ' + str(request))
            direction = request[0]
            distance = int(request[1:])
            for i in range(distance):
                self.move_one(direction)


    def move_one(self, direction):
        # Extend the path by 1 space in the given direction.  Also log that new coordinate in the history.
        if direction == 'U':
            self.coordinates[1] += 1
        elif direction == 'D':
            self.coordinates[1] -= 1
        elif direction == 'L':
            self.coordinates[0] -= 1
        elif direction == 'R':
            self.coordinates[0] += 1
        else:
            print('Invalid direction!')
            exit(1)
        self.log_coordinates()

    def log_coordinates(self):
        # Keep a history of where we have been
        # Convet the current coordinate list to a tuple which can then be saved into the set.
        self.history.add(tuple(self.coordinates))

    def get_coordinates(self):
        return self.coordinates

    def getX(self):
        return self.coordinates[0]

    def getY(self):
        return self.coordinates[1]

    def get_history(self):
        return self.history

def manhattan_distance(coordinateA, coordinateB):
    # Calculates the manhattan distance between two coordinates
    return abs(coordinateA[0] - coordinateB[0]) + abs(coordinateA[1] - coordinateB[1])

def find_overlaps(historyA, historyB):
    # Find the overlap (intersection) in two history sets.
    return historyA.intersection(historyB)

CENTRAL_PORT = Wire()
wire1 = Wire()
wire2 = Wire()

# print(wire1.get_coordinates())
# print(wire2.get_coordinates())
# print(manhattan_distance(wire1.get_coordinates(), wire2.get_coordinates()))

# wire1.alter_path('R8,U5,L5,D3')
# wire2.alter_path('U7,R6,D4,L4')

# wire1.alter_path('R75,D30,R83,U83,L12,D49,R71,U7,L72')
# wire2.alter_path('U62,R66,U55,R34,D71,R55,D58,R83')

# wire1.alter_path('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51')
# wire2.alter_path('U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')


# print()
# print(wire1.get_coordinates())
# print(wire2.get_coordinates())
# print(manhattan_distance(wire1.get_coordinates(), wire2.get_coordinates()))

# print()
# print(wire1.get_history())
# print(wire2.get_history())

# print()
# print(manhattan_distance(CENTRAL_PORT, wire1))
# print(manhattan_distance(CENTRAL_PORT, wire2))

inputs_path = 'input.txt'

with open(inputs_path) as input_file:
    PATH1=input_file.readline().rstrip()
    PATH2=input_file.readline().rstrip()

print('Applying path1')
wire1.alter_path(PATH1)
print('Applying path2')
wire2.alter_path(PATH2)

print('Finding overlaps')
overlap_distances = []
for overlap in find_overlaps(wire1.get_history(), wire2.get_history()):
    this_distance = manhattan_distance(CENTRAL_PORT.get_coordinates(), overlap)
    print(str(this_distance) + ' to ' + str(overlap))
    overlap_distances.append(this_distance)

print('Manhattan distance from CENTRAL_PORT to the closest intersection is ' + str(min(overlap_distances)))
