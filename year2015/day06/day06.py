import os
import sys


def get_action(direction):
    if "on" in direction:
        action = "on"
    elif "off" in direction:
        action = "off"
    elif "toggle" in direction:
        action = "toggle"
    else:
        sys.exit("Could not find an action!")

    return action


def get_start_and_end(positions):

    split_string = " through "

    start_position_string, end_position_string = positions.split(split_string)

    start_x, start_y = start_position_string.split(",")
    end_x, end_y = end_position_string.split(",")

    start_position = (int(start_x), int(start_y))
    end_position = (int(end_x), int(end_y))
    return start_position, end_position


def parse_direction(direction):
    # print(direction)
    action = get_action(direction)

    split_string = action + " "
    positions = direction.split(split_string)[1]

    start_position, end_position = get_start_and_end(positions)
    # print(action, start_position, end_position)
    return [action, start_position, end_position]


class LightGrid:
    def __init__(self, initial_state=0, width=1000, height=1000):
        self.initial_state = initial_state
        self.width = width
        self.height = height
        self.grid = [[self.initial_state for i in range(self.width)] for j in range(self.height)]

    def get_state(self, coordinate):
        x, y = coordinate

        return self.grid[x][y]

    def on(self, coordinate):
        x, y = coordinate
        # print(f"Turning on {coordinate}.")

        self.grid[x][y] = 1

    def off(self, coordinate):
        x, y = coordinate
        # print(f"Turning off {coordinate}.")

        self.grid[x][y] = 0

    def toggle(self, coordinate):
        x, y = coordinate
        # print(f"Toggle {coordinate}.")
        # print(x)
        # print(y)
        # print(self.grid[x][y])
        self.grid[x][y] = (self.grid[x][y] + 1) % 2

    def act_on_light(self, action, coordinate):
        if action == "on":
            self.on(coordinate)
        elif action == "off":
            self.off(coordinate)
        elif action == "toggle":
            self.toggle(coordinate)

    def act_on_section(self, action, start_coordinate, end_coordinate):
        # print("Got here")
        start_x, start_y = start_coordinate
        end_x, end_y = end_coordinate

        # print(f"for x in range({start_x}, {end_x}).")
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                # print(f"for y in range({start_y}, {end_y}).")
                # print("got here")
                light_coordinate = (x, y)
                self.act_on_light(action, light_coordinate)

    def print_raw(self):
        print(self.grid)

    def count_lit(self):
        lit_count = 0

        for x in range(0, self.width):
            for y in range(0, self.height):
                light_coordinate = (x, y)
                lit_count += self.get_state(light_coordinate)

        return lit_count


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    lights = LightGrid()

    with open(input_path) as input_file:
        for index, line in enumerate(input_file):
            this_direction = line.rstrip()
            print(index, this_direction)
            action, start, end = parse_direction(this_direction)
            # print(action, start, end)
            lights.act_on_section(action, start, end)

    print(lights.count_lit())
    # lights.print_raw()
    # print(lights.get_state((1, 2)))
    # lights.on((1,2))
    # print(lights.get_state((1, 2)))
    # lights.toggle((1,2))
    # print(lights.get_state((1, 2)))
    # lights.toggle((1,2))
    # print(lights.get_state((1, 2)))
    # lights.off((1,2))
    # print(lights.get_state((1, 2)))
    # lights.off((1,2))
    # print(lights.get_state((1, 2)))
