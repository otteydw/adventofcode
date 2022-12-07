import os
import pandas
import numpy

def load_from_file(filename):
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

# def fix_boxes(original_boxes):
#     new_boxes = []

#     for row in original_boxes:
#         new_row=[]
#         for box in row:
#             if box == numpy.NAN:
#                 box = ''
#             # else:
#             #     box.translate({ord(i): None for i in '[]'})
#             new_row.append(box)
#         new_boxes.append(row)
#     return new_boxes

if __name__ == "__main__":

    # input_filename = "input.txt"
    input_filename = "example.txt"

    boxes, moves = load_from_file(input_filename)

    # boxes.reverse()
    for line in boxes:
        print(line)
    # print(boxes)
    # boxes = fix_boxes(boxes)
    # for line in boxes:
    #     print(line)
    # pandas.read_fwf('tmpout.tmp')

    # print(moves)