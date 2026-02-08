# mypy: ignore-errors
import os


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
        self.process_program()

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

    def signal_strength(self, cycle):
        # "During" means the value at the end of the previous cycle
        return cycle * self.X_history[cycle - 1]

    def sum_of_signal_strengths(self, signals):
        sum = 0
        for signal in signals:
            sum += self.signal_strength(signal)
        return sum

    def draw(self):
        width = 40
        height = 6
        screen = [["."] * width for i in range(height)]

        for cycle in range(240):
            row = cycle // width
            column = cycle % width
            sprite_middle = self.X_history[cycle]

            if column in [sprite_middle - 1, sprite_middle, sprite_middle + 1]:
                screen[row][column] = "#"

        for row in screen:
            for column in row:
                print(column, end="")
            print()


if __name__ == "__main__":

    # input_filename = "small_program.txt"
    # input_filename = "larger_program.txt"
    input_filename = "input.txt"

    tube = Tube(input_filename)

    interesting_signals = [20, 60, 100, 140, 180, 220]
    print(f"Sum of signals: {tube.sum_of_signal_strengths(interesting_signals)}")
    print()
    tube.draw()
