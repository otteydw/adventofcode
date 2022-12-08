import os
import pandas

# import pyparsing as pp

class Supplies:
    def __init__(self, filename):
        self.boxes, self.moves = self.load_from_file(filename)
        # print(self.boxes)
        self.process_moves()
        # print(self.boxes)

    def load_from_file(self, filename):
        input_path = os.path.join(os.path.dirname(__file__), filename)
        tmp_output_path = os.path.join(os.path.dirname(__file__), 'tmpout.tmp')

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
        with open(tmp_output_path, "w") as output_file:
            for line in boxes:
                output_file.write(line + '\n')

        boxes_df = pandas.DataFrame.transpose(pandas.read_fwf('tmpout.tmp')).fillna('')
        boxes_df = boxes_df.replace('\[|\]', '', regex=True)
        boxes_list = boxes_df.values.tolist()

        stripped_boxes = []
        for column in boxes_list:
            new_column = [i for i in column if i]   # removes the empty strings
            stripped_boxes.append(new_column)
        return stripped_boxes, moves

    def process_moves(self):
        # move_pattern = "move" + pp.Word(pp.nums) + "from" + pp.Word(pp.nums) + "to" + pp.Word(pp.nums)
        for move in self.moves:
            # print(move)
            # this_move = move_pattern.parse_string(move)
            # print(this_move)
            move = move.split(' ')
            quantity_to_move = int(move[1])
            from_stack = int(move[3]) - 1
            to_stack = int(move[5]) - 1
            # print(quantity_to_move, from_stack, to_stack)

            for _ in range(0, quantity_to_move):
                crate = self.boxes[from_stack].pop()
                self.boxes[to_stack].append(crate)

    def see_top_crates(self):
        top_crates = ""
        for stack in self.boxes:
            top_crates += stack[-1:][0]
        return top_crates

if __name__ == "__main__":

    input_filename = "input.txt"
    # input_filename = "example.txt"

    my_supplies = Supplies(input_filename)
    print(f"Top crates: {my_supplies.see_top_crates()}")
    # boxes, moves = load_from_file(input_filename)

    # # boxes.reverse()
    # for line in boxes:
    #     print(line)

    # # print(moves)