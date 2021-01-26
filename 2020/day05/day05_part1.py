
# https://adventofcode.com/2020/day/5

def get_passes_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    passes = [x.strip() for x in lines]
    # print(passes)
    return passes

def get_seat_id(row, column):
    return row*8 + column

# def get_row(decoded_pass):
#     return decoded_pass[0]

# def get_column(decoded_pass):
#     return decoded_pass[1]

def display_pass(decoded_pass):
    # row = get_row(decoded_pass)
    # column = get_column(decoded_pass)
    row = decoded_pass[0]
    column = decoded_pass[1]
    print("row " + str(row) + ", column " + str(column) + ", seat ID " + str(get_seat_id(row, column)))

def decode_boarding_pass(boarding_pass):
    row = get_row(boarding_pass)
    column = get_column(boarding_pass)
    return (row, column)

def decode_front_back(letter):
    return letter == 'B'

def convert_fb_to_binary(some_string):
    return some_string.replace("F", "0").replace("B", "1")

def convert_lr_to_binary(some_string):
    return some_string.replace("L", "0").replace("R", "1")

def get_row(boarding_pass):

    row_binary = convert_fb_to_binary(boarding_pass[0:7])
    # print(row_binary)
    return int(row_binary, 2)

def get_column(boarding_pass):

    column_binary = convert_lr_to_binary(boarding_pass[7:10])
    # print(column_binary)
    return int(column_binary, 2)

def main():
    # FILENAME='invalids.txt'
    # FILENAME='valids.txt'
    FILENAME='input.txt'
    passes = get_passes_from_file(FILENAME)

    # boarding_pass = 'BFFFBBFRRR' # row 70, column 7, seat ID 567.
    # boarding_pass = 'FFFBBBFRRR' # row 14, column 7, seat ID 119.
    # boarding_pass = 'BBFFBBFRLL' # row 102, column 4, seat ID 820.

    highest_seat_id = 0

    for encoded_boarding_pass in passes:
        decoded_pass = decode_boarding_pass(encoded_boarding_pass)
        print(decoded_pass)
        display_pass(decoded_pass)
    #     this_seat_id = get_seat_id(decoded_pass)
    #     if this_seat_id > highest_seat_id:
    #         highest_seat_id = this_seat_id

    # print()
    # print("Highest seat ID: " + str(highest_seat_id))

    # print(get_row(boarding_pass))
    # print(get_column(boarding_pass))
    # valid_batch_count = 0
    # for batch in batches:
    #     if isValidBatch(batch):
    #         valid_batch_count += 1

    # print(valid_batch_count)

main()