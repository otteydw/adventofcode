import os
import tempfile
from typing import Any

import pandas


class Supplies:
    def __init__(self, filename: str):
        self.boxes, self.moves = self.load_from_file(filename)

    def load_from_file(self, filename: str) -> tuple[list[list[Any]], list[str]]:
        input_path = os.path.join(os.path.dirname(__file__), filename)

        boxes = []
        moves = []
        after_newline = False

        with open(input_path) as input_file:
            for line in input_file:
                line_stripped = line.rstrip()
                if line_stripped == "":
                    after_newline = True
                    continue
                if after_newline:
                    moves.append(line_stripped)

                else:
                    boxes.append(line_stripped)

        boxes.reverse()

        with tempfile.NamedTemporaryFile(mode="w+t") as output_file:
            for line in boxes:
                output_file.write(line + "\n")

            output_file.flush()
            boxes_df = pandas.DataFrame.transpose(pandas.read_fwf(output_file.name)).fillna("")

        boxes_df = boxes_df.replace(r"\[|\]", "", regex=True)
        boxes_list = boxes_df.values.tolist()

        stripped_boxes = []
        for column in boxes_list:
            new_column = [i for i in column if i]  # removes the empty strings
            stripped_boxes.append(new_column)
        return stripped_boxes, moves

    def process_moves(self, crane: int = 9000) -> None:
        for move in self.moves:
            _move = move.split(" ")
            quantity_to_move = int(_move[1])
            from_stack = int(_move[3]) - 1
            to_stack = int(_move[5]) - 1

            crates_to_move = []
            for _ in range(0, quantity_to_move):
                crate = self.boxes[from_stack].pop()
                crates_to_move.append(crate)
            if crane == 9001:
                crates_to_move.reverse()
            for crate in crates_to_move:
                self.boxes[to_stack].append(crate)

    def see_top_crates(self) -> str:
        top_crates = ""
        for stack in self.boxes:
            top_crates += stack[-1:][0]
        return top_crates


if __name__ == "__main__":

    input_filename = "input.txt"

    my_supplies = Supplies(input_filename)
    my_supplies.process_moves()
    print(f"Top crates: {my_supplies.see_top_crates()}")

    my_supplies = Supplies(input_filename)
    my_supplies.process_moves(crane=9001)
    print(f"Top crates (crane 9001): {my_supplies.see_top_crates()}")
