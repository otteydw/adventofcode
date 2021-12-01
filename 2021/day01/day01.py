import os

def load_ints_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__),filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(int(line.rstrip()))

    return data

def count_depth_increases(depths):

    depth_increase_count = 0
    previous_depth = depths[0]

    for current_depth in depths[1:]:
        if current_depth > previous_depth:
            depth_increase_count += 1
        previous_depth = current_depth

    return depth_increase_count

if __name__ == "__main__":

    depths = load_ints_from_file("input.txt")
    print(f"{count_depth_increases(depths)} measurements are larger than the previous measurement.")