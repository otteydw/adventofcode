import math
import os

import pandas as pd


def load_ints_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

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


def count_sum_of_sliding_window_increases(list_depths, window_length=3):
    df_depths = pd.DataFrame(list_depths, columns=["Depth"])

    df_depths["rolling_sum"] = df_depths.rolling(window_length, min_periods=window_length).sum()

    window_sums = [x for x in df_depths["rolling_sum"].values if math.isnan(x) == False]

    return count_depth_increases(window_sums)


if __name__ == "__main__":

    depths = load_ints_from_file("input.txt")
    print(f"{count_depth_increases(depths)} measurements are larger than the previous measurement.")
    print(
        f"{count_sum_of_sliding_window_increases(depths)} measurement windows are larger than the previous measurement window."
    )
