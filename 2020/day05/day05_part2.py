
# https://adventofcode.com/2020/day/5

def get_passes_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    passes = [x.strip() for x in lines]
    return passes

def get_row_column_from_decoded_pass(decoded_pass):
    row = get_row_from_decoded_pass(decoded_pass)
    column = get_column_from_decoded_pass(decoded_pass)
    return row, column

def get_seat_id_from_decoded_pass(decoded_pass):
    row, column = get_row_column_from_decoded_pass(decoded_pass)
    return row*8 + column

def get_row_from_decoded_pass(decoded_pass):
    return decoded_pass[0]

def get_column_from_decoded_pass(decoded_pass):
    return decoded_pass[1]

def display_pass(decoded_pass):
    row, column = get_row_column_from_decoded_pass(decoded_pass)
    print("row " + str(row) + ", column " + str(column) + ", seat ID " + str(get_seat_id_from_decoded_pass(decoded_pass)))

def decode_boarding_pass(encoded_boarding_pass):
    row = get_row(encoded_boarding_pass)
    column = get_column(encoded_boarding_pass)
    return (row, column)

def decode_front_back(letter):
    return letter == 'B'

def convert_fb_to_binary(some_string):
    return some_string.replace("F", "0").replace("B", "1")

def convert_lr_to_binary(some_string):
    return some_string.replace("L", "0").replace("R", "1")

def get_row(boarding_pass):

    row_binary = convert_fb_to_binary(boarding_pass[0:7])
    return int(row_binary, 2)

def get_column(boarding_pass):

    column_binary = convert_lr_to_binary(boarding_pass[7:10])
    return int(column_binary, 2)

def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]

def main():
    FILENAME='input.txt'
    passes = get_passes_from_file(FILENAME)

    # boarding_pass = 'BFFFBBFRRR' # row 70, column 7, seat ID 567.
    # boarding_pass = 'FFFBBBFRRR' # row 14, column 7, seat ID 119.
    # boarding_pass = 'BBFFBBFRLL' # row 102, column 4, seat ID 820.

    seat_ids = []

    for encoded_boarding_pass in passes:
        decoded_pass = decode_boarding_pass(encoded_boarding_pass)
        # display_pass(decoded_pass)
        this_seat_id = get_seat_id_from_decoded_pass(decoded_pass)
        seat_ids.append(this_seat_id)

    # print()
    # print(sorted(seat_ids))
    my_seat_id = find_missing(sorted(seat_ids))
    print("My seat id: " + str(my_seat_id))

main()