import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


def convert_assignment(assignment):
    assignment_start = int(assignment.split("-")[0])
    assignment_end = int(assignment.split("-")[1])
    return (assignment_start, assignment_end)


def parse_section_assignments(raw_data):
    section_assignments = []
    for line in raw_data:
        assignment1, assignment2 = line.split(",")
        assignment1 = convert_assignment(assignment1)
        assignment2 = convert_assignment(assignment2)
        section_assignments.append((assignment1, assignment2))
    return section_assignments


def check_overlap(assignment1, assignment2, any_overlap=False):
    if any_overlap:
        if assignment1[0] <= assignment2[0] and assignment1[1] >= assignment2[0]:
            return True
        elif assignment2[0] <= assignment1[0] and assignment2[1] >= assignment1[0]:
            return True
    else:
        if assignment1[0] <= assignment2[0] and assignment1[1] >= assignment2[1]:
            return True
        elif assignment2[0] <= assignment1[0] and assignment2[1] >= assignment1[1]:
            return True
    return False


def count_overlaps(assignments, any_overlap=False):
    overlap_count = 0
    for assignment in assignments:
        if check_overlap(assignment[0], assignment[1], any_overlap=any_overlap):
            overlap_count += 1
    return overlap_count


if __name__ == "__main__":

    input_filename = "input.txt"

    data = load_from_file(input_filename)

    assignments = parse_section_assignments(data)
    print(f"Number of overlaps is {count_overlaps(assignments)}")
    print(f"Number of overlaps (any) is {count_overlaps(assignments, any_overlap=True)}")
