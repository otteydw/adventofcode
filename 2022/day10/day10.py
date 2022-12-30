import os
import pprint


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data

class Tube:
    def __init__(self, filename):
        self.program = load_from_file(filename)
        self.X = 1
        self.X_history = {}
        self.cycles = 0
        self.update_register()
        # self.status_report()
        self.process_program()
        # self.status_report()

    def process_program(self):
        for instruction in self.program:
            if instruction == "noop":
                self.cycles += 1
                self.update_register()
            elif instruction.startswith("addx"):
                ticks = 2
                for _ in range(ticks):
                    self.cycles += 1
                    self.update_register()
                self.X += int(instruction.split(" ")[1])
                self.update_register()

    def update_register(self):
        self.X_history[self.cycles] = self.X

    def status_report(self):
        pprint.pprint(self.X_history)

    def signal_strength(self, cycle):
        # "During" means the value at the end of the previous cycle
        return cycle * self.X_history[cycle-1]

    def sum_of_signal_strengths(self, signals):
        sum = 0
        for signal in signals:
            sum += self.signal_strength(signal)
        return sum

if __name__ == "__main__":

    # input_filename = "small_program.txt"
    input_filename = "input.txt"

    tube = Tube(input_filename)
    # for knots in [2, 10]:
    #     rope = Rope(input_filename, knots=knots)
    #     print(
    #         f"Rope with {knots} knots: Tail visited {rope.count_tail_visited_positions()} positions."
    #     )
    # tube.status_report()
    interesting_signals=[20, 60, 100, 140, 180, 220]
    print(f"Sum of signals: {tube.sum_of_signal_strengths(interesting_signals)}")