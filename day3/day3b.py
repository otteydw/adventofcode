#!/usr/bin/python3

# https://adventofcode.com/2019/day/3

# --- Part Two ---
# It turns out that this circuit is very timing-sensitive; you actually need to
# minimize the signal delay.

# To do this, calculate the number of steps each wire takes to reach each
# intersection; choose the intersection where the sum of both wires' steps is
# lowest. If a wire visits a position on the grid multiple times, use the steps
# value from the first time it visits that position when calculating the total
# value of a specific intersection.

# The number of steps a wire takes is the total number of grid squares the wire
# has entered to get to that location, including the intersection being
# considered. Again consider the example from above:

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
# In the above example, the intersection closest to the central port is reached
# after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the
# second wire for a total of 20+20 = 40 steps.

# However, the top-right intersection is better: the first wire takes only 8+5+2
# = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

# Here are the best steps for the extra examples from above:

# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps

# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

# What is the fewest combined steps the wires must take to reach an intersection?

class Wire():

    def __init__(self):
        self.coordinates = [0, 0]   # Use a list because tuples cannot be modified.
        self.steps = 0              # The total steps this wire has taken.
        self.history = set()        # Use a set because we do not care about duplicates, and sets are much faster to parse than lists.
        self.history_with_steps = {}    # A dictionary containing the shortest step count to reach a specific coordinate

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
        self.steps += 1
        self.log_coordinates()

    def log_coordinates(self):
        # Keep a history of where we have been
        # Convert the current coordinate list to a tuple which can then be saved into the set.
        if tuple(self.coordinates) not in self.history:
            # Record the shortest number of steps to get to this coordinate.
            self.history_with_steps[tuple(self.coordinates)] = self.steps
            # Add this coordinate to the history.  Might be redundant to above, but it works from part 1.
            self.history.add(tuple(self.coordinates))

    def get_coordinates(self):
        return self.coordinates

    def getX(self):
        return self.coordinates[0]

    def getY(self):
        return self.coordinates[1]

    def get_history(self):
        return self.history

    def get_history_with_steps(self):
        return self.history_with_steps

    def signal_delay(self, coordinate):
        # Report the "signal delay" for the wire to get to a specific coordinate
        return self.get_history_with_steps()[coordinate]


def manhattan_distance(coordinateA, coordinateB):
    # Calculates the manhattan distance between two coordinates
    return abs(coordinateA[0] - coordinateB[0]) + abs(coordinateA[1] - coordinateB[1])

def total_signal_delay(wireA, wireB, coordinate):
    # Given two wires and a coordinate, return the combined signal delay.
    return wireA.signal_delay(coordinate) + wireB.signal_delay(coordinate)

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
overlap_signal_delays = []
for overlap in find_overlaps(wire1.get_history(), wire2.get_history()):
    this_distance = manhattan_distance(CENTRAL_PORT.get_coordinates(), overlap)
    this_delay = total_signal_delay(wire1, wire2, overlap)
    print(str(overlap) + ': Manhattan = ' + str(this_distance) + ', Signal Delay = ' + str(this_delay))
    overlap_distances.append(this_distance)
    overlap_signal_delays.append(this_delay)

print()
print('Shortest manhattan distance from CENTRAL_PORT to the closest intersection is ' + str(min(overlap_distances)))
print('Shortest signal delay from CENTRAL_PORT is ' + str(min(overlap_signal_delays)))

# print(wire1.get_history_with_steps())
# print(wire1.signal_delay((8, 2)))