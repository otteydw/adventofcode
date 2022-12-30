import logging
import os

logging.basicConfig(level=logging.INFO)

def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data

class Knot:
    def __init__(self):
        self.position = (0, 0)

    def move(self, direction):
        # logging.debug(f"Move knot {direction} {distance}")

        if direction == "L":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "R":
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "U":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "D":
            self.position = (self.position[0], self.position[1] - 1)

    def follow(self, position_to_follow):
        if not self.is_touching(position_to_follow):
            # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough
            if position_to_follow[0] == self.position[0]:
                if position_to_follow[1] - self.position[1] == 2:
                    self.move("U")
                elif position_to_follow[1] - self.position[1] == -2:
                    self.move("D")
            elif position_to_follow[1] == self.position[1]:
                if position_to_follow[0] - self.position[0] == 2:
                    self.move("R")
                elif position_to_follow[0] - self.position[0] == -2:
                    self.move("L")
            # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
            else:
                if position_to_follow[0] > self.position[0]:
                    self.move("R")
                else:
                    self.move("L")
                if position_to_follow[1] > self.position[1]:
                    self.move("U")
                else:
                    self.move("D")

    def is_touching(self, position_to_compare):
        return (
            abs(self.position[0] - position_to_compare[0]) <= 1
            and abs(self.position[1] - position_to_compare[1]) <= 1
        )
class Rope:
    def __init__(self, filename, knots=2):
        self.motions = load_from_file(filename)
        self.knots = []
        for _ in range(knots):
            knot = Knot()
            self.knots.append(knot)
        self.tail_visited_positions = set()
        self.record_tail_visit()
        self.status_report()
        self.process_motions()

    def get_head_position(self):
        return self.knots[0].position

    def get_tail_position(self):
        return self.knots[-1].position

    def status_report(self):
        logging.debug(f"Current head: {self.get_head_position()}")
        logging.debug(f"Current tail: {self.get_tail_position()}")
        logging.debug(f"Visited: {self.tail_visited_positions}")
        logging.debug(f"-------------------------------------------------")

    def record_tail_visit(self):
        self.tail_visited_positions.add(self.get_tail_position())

    def count_tail_visited_positions(self):
        return len(self.tail_visited_positions)

    def move_head(self, direction, distance):
        logging.debug(f"Move head {direction} {distance}")

        for _ in range(distance):
            for knot_number, knot in enumerate(self.knots):
                if knot_number == 0:
                    knot.move(direction)
                else:
                    knot.follow(self.knots[knot_number-1].position)
            self.record_tail_visit()


    # def check_head_tail_touching(self):
    #     return (
    #         abs(self.head_position[0] - self.tail_position[0]) <= 1
    #         and abs(self.head_position[1] - self.tail_position[1]) <= 1
    #     )

    # def move_tail(self, direction, distance):
    #     logging.debug(f"Move tail {direction} {distance}")

    #     for _ in range(distance):
    #         if direction == "L":
    #             self.tail_position = (self.tail_position[0] - 1, self.tail_position[1])
    #         elif direction == "R":
    #             self.tail_position = (self.tail_position[0] + 1, self.tail_position[1])
    #         elif direction == "U":
    #             self.tail_position = (self.tail_position[0], self.tail_position[1] + 1)
    #         elif direction == "D":
    #             self.tail_position = (self.tail_position[0], self.tail_position[1] - 1)

    # def update_tail(self):
    #     # if not self.check_head_tail_touching():
    #     #     # If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough
    #     #     if self.head_position[0] == self.tail_position[0]:
    #     #         if self.head_position[1] - self.tail_position[1] == 2:
    #     #             self.move_tail("U", 1)
    #     #         elif self.head_position[1] - self.tail_position[1] == -2:
    #     #             self.move_tail("D", 1)
    #     #     elif self.head_position[1] == self.tail_position[1]:
    #     #         if self.head_position[0] - self.tail_position[0] == 2:
    #     #             self.move_tail("R", 1)
    #     #         elif self.head_position[0] - self.tail_position[0] == -2:
    #     #             self.move_tail("L", 1)
    #     #     # Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up
    #     #     else:
    #     #         if self.head_position[0] > self.tail_position[0]:
    #     #             self.move_tail("R", 1)
    #     #         else:
    #     #             self.move_tail("L", 1)
    #     #         if self.head_position[1] > self.tail_position[1]:
    #     #             self.move_tail("U", 1)
    #     #         else:
    #     #             self.move_tail("D", 1)
    #     self.record_tail_visit()
    #     self.status_report()

    def process_motions(self):
        for motion in self.motions:
            direction, distance = motion.split(" ")
            distance = int(distance)
            self.move_head(direction, distance)


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    rope = Rope(input_filename, knots=2)
    # rope.status_report()
    print(f"Knots: 2 | Tail visited {rope.count_tail_visited_positions()} positions.")
    # print(f"Visible trees: {forest.count_visible_trees()}")
    # print(f"Highest scenic score: {forest.highest_scenic_score()}")
    rope = Rope(input_filename, knots=10)
    print(f"Knots: 10 | Tail visited {rope.count_tail_visited_positions()} positions.")
