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

    def isValid_year(year):
        return len(str(year)) == 4

    def isValid_byr(year):
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        return isValid_year(year) and 1920 <= int(year) <= 2002

    def isValid_iyr(year):
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        return isValid_year(year) and 2010 <= int(year) <= 2020

    def isValid_eyr(year):
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return isValid_year(year) and 2020 <= int(year) <= 2030

    def isValid_hgt(height):
        # hgt (Height) - a number followed by either cm or in:

        def unit(height):
            return height[-2:]

        def height_value(height):
            return int(height[:-2])

        if unit(height) == "in":
            # If in, the number must be at least 59 and at most 76.
            return 59 <= height_value(height) <= 76
        if unit(height) == "cm":
            # If cm, the number must be at least 150 and at most 193.
            return 150 <= height_value(height) <= 193
        return False

    def isValid_hcl(color_code):
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        return (
            color_code[0] == "#"
            and len(color_code) == 7
            and set(color_code[1:]).issubset(
                set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"])
            )
        )

    def isValid_ecl(color_word):
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        return color_word in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def isValid_pid(passport_id):
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        return len(passport_id) == 9 and passport_id.isdigit()

    # cid (Country ID) - ignored, missing or not.

    def contains_required_fields(batch):
        REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return set(REQUIRED_FIELDS).issubset(set(batch.keys()))

    return (
        contains_required_fields(batch)
        and isValid_byr(batch["byr"])
        and isValid_iyr(batch["iyr"])
        and isValid_eyr(batch["eyr"])
        and isValid_hgt(batch["hgt"])
        and isValid_hcl(batch["hcl"])
        and isValid_ecl(batch["ecl"])
        and isValid_pid(batch["pid"])
    )


def main():
    # FILENAME='invalids.txt'
    # FILENAME='valids.txt'
    FILENAME = "input.txt"
    batches = get_batches_from_file(FILENAME)

    valid_batch_count = 0
    for batch in batches:
        if isValidBatch(batch):
            valid_batch_count += 1

    print(valid_batch_count)


main()
