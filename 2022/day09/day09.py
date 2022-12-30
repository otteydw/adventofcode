import os

DEBUG = 0


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


class Rope:
    def __init__(self, filename):
        self.motions = load_from_file(filename)
        self.head_position = (0, 0)
        self.tail_position = (0, 0)
        self.tail_visited_positions = set()
        self.record_tail_visit()
        if DEBUG == 1:
            self.status_report()
        self.process_motions()

    def status_report(self):
        print(f"Current head: {self.head_position}")
        print(f"Current tail: {self.tail_position}")
        print(f"Visited: {self.tail_visited_positions}")
        print(f"-------------------------------------------------")

    def record_tail_visit(self):
        self.tail_visited_positions.add(self.tail_position)

    def count_tail_visited_positions(self):
        return len(self.tail_visited_positions)

    def move_head(self, direction, distance):
        if DEBUG == 1:
            print(f"Move head {direction} {distance}")
        # head_x, head_y = self.head_position[0], self.head_position[1]

        for _ in range(distance):
            if direction == "L":
                self.head_position = (self.head_position[0] - 1, self.head_position[1])
            elif direction == "R":
                self.head_position = (self.head_position[0] + 1, self.head_position[1])
            elif direction == "U":
                self.head_position = (self.head_position[0], self.head_position[1] + 1)
            elif direction == "D":
                self.head_position = (self.head_position[0], self.head_position[1] - 1)

            self.update_tail()

    def check_head_tail_touching(self):
        # head_x = self.head_position[0]
        # head_y = self.head_position[1]
        # tail_x = self.tail_position[0]
        # tail_y = self.tail_position[1]
        # print(f"Head: {head_x}, {head_y} | Tail: {tail_x}, {tail_y}")
        return (
            abs(self.head_position[0] - self.tail_position[0]) <= 1
            and abs(self.head_position[1] - self.tail_position[1]) <= 1
        )

    def move_tail(self, direction, distance):
        if DEBUG == 1:
            print(f"Move tail {direction} {distance}")
        # tail_x, tail_y = self.tail_position[0], self.tail_position[1]

        for _ in range(distance):
            if direction == "L":
                self.tail_position = (self.tail_position[0] - 1, self.tail_position[1])
            elif direction == "R":
                self.tail_position = (self.tail_position[0] + 1, self.tail_position[1])
            elif direction == "U":
                self.tail_position = (self.tail_position[0], self.tail_position[1] + 1)
            elif direction == "D":
                self.tail_position = (self.tail_position[0], self.tail_position[1] - 1)

    def update_tail(self):
        if not self.check_head_tail_touching():
            # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough
            if self.head_position[0] == self.tail_position[0]:
                if self.head_position[1] - self.tail_position[1] == 2:
                    self.move_tail("U", 1)
                elif self.head_position[1] - self.tail_position[1] == -2:
                    self.move_tail("D", 1)
            elif self.head_position[1] == self.tail_position[1]:
                if self.head_position[0] - self.tail_position[0] == 2:
                    self.move_tail("R", 1)
                elif self.head_position[0] - self.tail_position[0] == -2:
                    self.move_tail("L", 1)
            # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
            else:
                if self.head_position[0] > self.tail_position[0]:
                    self.move_tail("R", 1)
                else:
                    self.move_tail("L", 1)
                if self.head_position[1] > self.tail_position[1]:
                    self.move_tail("U", 1)
                else:
                    self.move_tail("D", 1)
        self.record_tail_visit()
        if DEBUG == 1:
            self.status_report()

    def process_motions(self):
        for motion in self.motions:
            direction, distance = motion.split(" ")
            distance = int(distance)
            self.move_head(direction, distance)


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    rope = Rope(input_filename)
    if DEBUG == 1:
        rope.status_report()
    print(f"Tail visited {rope.count_tail_visited_positions()} positions.")
    # print(f"Visible trees: {forest.count_visible_trees()}")
    # print(f"Highest scenic score: {forest.highest_scenic_score()}")
