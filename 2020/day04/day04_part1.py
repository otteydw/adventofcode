
# https://adventofcode.com/2020/day/4

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def isBlank(myString):
    return not (myString and myString.strip())

def get_fields_from_line(line):
    fields_in_line = []
    # fields_in_line = {}
    key_values = line.split(' ')
    for key_value in key_values:
        key, value = key_value.strip().split(':')
        fields_in_line.append([key, value])
        # fields_in_line[key] = value
        # print(key, value)
    # print(fields_in_line)
    return fields_in_line

def get_batches_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    batches = []

    batch = {}
    for line in lines:
        if not isBlank(line):
            # batch.append(get_fields_from_line(line))
            # batch = batch + get_fields_from_line(line)
            # print(batch)
            for key, value in get_fields_from_line(line):
                # print(key, value)
                batch[key] = value
        else:
            batches.append(batch)
            batch = {}
    batches.append(batch) # Get the last one

    # print(batches)
    # for batch in batches:
    #     print(batch)

    return batches

def isValidBatch(batch):
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # cid is optional

    print(set(REQUIRED_FIELDS))
    print(set(batch.keys()))

    if set(REQUIRED_FIELDS).issubset(set(batch.keys())):
        print('yes')
        print()
        return True
    else:
        print('no')
        print()
        return False
    # print(batch.keys())
    # return True



def main():
    # batches = get_batches_from_file('example.txt')
    batches = get_batches_from_file('input.txt')

    # print(batches)

    valid_batch_count = 0
    for batch in batches:
        if isValidBatch(batch):
            valid_batch_count += 1

    print(valid_batch_count)
    # lines = [x.strip() for x in lines]
    # map = []

    # for line in lines:
    #     print(line)

    # tree_mult = 1

    # for right, down in [(1, 1), (3, 1), (5,1), (7,1),(1,2)]:
    #     tree_mult = tree_mult * trees_in_slope(right, down, map)

    # print(tree_mult)

main()