import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


class Node:
    def __init__(self, name, type, parent, size=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0
        self.type = type

        if self.isFile():
            self.increase_size(size)

    def increase_size(self, size):
        self.size += size
        if self.parent != None:
            self.parent.increase_size(size)

    def get_size(self):
        return self.size

    def get_type(self):
        return self.type

    def isDirectory(self):
        return self.type == "directory"

    def isFile(self):
        return self.type == "file"

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self, indent=0):
        if self.isDirectory():
            print(" " * indent + "- " + self.name + " (dir) " + str(self.size))
            for child in self.children:
                child.print_tree(indent + 2)
        else:
            print(" " * indent + "- " + self.name + " (file, size=" + str(self.size) + ")")

    def get_directories(self):
        list_of_directories = []

        if self.isDirectory():
            list_of_directories.append(self)
            for child in self.children:
                list_of_directories += child.get_directories()
        return list_of_directories

    def sum_dirs_under_size(self, max_size):
        list_of_dirs = self.get_directories()

        sum_size = 0

        for dir in list_of_dirs:
            if dir.size <= max_size:
                sum_size += dir.size

        return sum_size


def parse_terminal_output(terminal_output, current_dir=None):

    if current_dir == None:
        root = Node("/", "directory", None)
        current_directory = root
    else:
        current_directory = current_dir

    for line in terminal_output:
        if line.startswith("$ cd"):
            dir_name = line.split(" ")[2]
            if dir_name == "..":
                current_directory = current_directory.parent
            for child in current_directory.children:
                if child.name == dir_name:
                    current_directory = child
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir "):
            new_dir_name = line.split(" ")[1]
            new_dir = Node(new_dir_name, "directory", current_directory)
            current_directory.add_child(new_dir)
        else:
            file_size, file_name = line.split(" ")
            new_file = Node(file_name, "file", current_directory, int(file_size))
            current_directory.add_child(new_file)

    return root


def get_unused_space(root, total_disk_space=70000000):
    return total_disk_space - root.size


def get_space_to_free(root, total_space_needed=30000000):
    return total_space_needed - get_unused_space(root)


def size_of_dir_to_delete(root: Node, total_disk_space=70000000, total_space_needed=30000000):
    space_to_free = get_space_to_free(root)
    smallest_size_found = total_disk_space + 1  # some large number
    for dir in root.get_directories():
        if dir.size >= space_to_free and dir.size < smallest_size_found:
            smallest_size_found = dir.size

    return smallest_size_found


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    data = load_from_file(input_filename)

    filesystem = parse_terminal_output(data)
    filesystem.print_tree()
    print(f"Sum of dirs under size: {filesystem.sum_dirs_under_size(100000)}")
    print(f"Size of directory to delete: {size_of_dir_to_delete(filesystem)}")
