# mypy: ignore-errors
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
    key_values = line.split(" ")
    for key_value in key_values:
        key, value = key_value.strip().split(":")
        fields_in_line.append([key, value])
    return fields_in_line


def get_batches_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    batches = []

    batch = {}
    for line in lines:
        if not isBlank(line):
            for key, value in get_fields_from_line(line):
                batch[key] = value
        else:
            batches.append(batch)
            batch = {}
    batches.append(batch)  # Get the last one

    return batches


def isValidBatch(batch):
    REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    # cid is optional

    return set(REQUIRED_FIELDS).issubset(set(batch.keys()))


def main():
    batches = get_batches_from_file("input.txt")

    valid_batch_count = 0
    for batch in batches:
        if isValidBatch(batch):
            valid_batch_count += 1

    print(valid_batch_count)


main()
