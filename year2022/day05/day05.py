import os
import tempfile

import pandas


class Supplies:
    def __init__(self, filename):
        self.boxes, self.moves = self.load_from_file(filename)

    def load_from_file(self, filename):
        tmp_filename = "tmpout.tmp"
        input_path = os.path.join(os.path.dirname(__file__), filename)
        # tmp_output_path = os.path.join(os.path.dirname(__file__), tmp_filename)

        with tempfile.NamedTemporaryFile(mode="w+t", delete_on_close=False, delete=False) as output_file:
            tmp_filename = output_file.name
            print(f"{tmp_filename=}")

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
            # with open(tmp_output_path, "w") as output_file:
            for line in boxes:
                output_file.write(line + "\n")

            output_file.flush()
            boxes_df = pandas.DataFrame.transpose(pandas.read_fwf(tmp_filename)).fillna("")
            # os.remove(tmp_filename)
        boxes_df = boxes_df.replace(r"\[|\]", "", regex=True)
        boxes_list = boxes_df.values.tolist()

        stripped_boxes = []
        for column in boxes_list:
            new_column = [i for i in column if i]  # removes the empty strings
            stripped_boxes.append(new_column)
        return stripped_boxes, moves

    def process_moves(self, crane=9000):
        for move in self.moves:
            move = move.split(" ")
            quantity_to_move = int(move[1])
            from_stack = int(move[3]) - 1
            to_stack = int(move[5]) - 1

            crates_to_move = []
            for _ in range(0, quantity_to_move):
                crate = self.boxes[from_stack].pop()
                crates_to_move.append(crate)
            if crane == 9001:
                crates_to_move.reverse()
            for crate in crates_to_move:
                self.boxes[to_stack].append(crate)

    def see_top_crates(self):
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
