import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

class Directory(Node):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.children = []
        # self.size = 0

    def add(self, child):
        self.children.append(child)

class File(Node):
    def __init__(self, name, parent, size=0):
        super().__init__(name, parent)
        self.size=size
        # self.parent.size += self.size

def print_tree(root, indent=0):
    # print(' '*indent + '- ' + root.name)
    if hasattr(root, 'children'):
        print(' '*indent + '- ' + root.name + ' (dir)')
        for child in root.children:
            print_tree(child, indent+2)
    else:
        print(' '*indent + '- ' + root.name + ' (file, size=' + str(root.size) + ')')

def parse_terminal_output(terminal_output, current_dir=None):

    if current_dir == None:
        # current_directory = None
        root = Directory('/', None)
        current_directory = root
    else:
        current_directory=current_dir

    for line in terminal_output:
        if line.startswith('$ cd'):
            dir_name = line.split(' ')[2]
            if dir_name == '..':
                current_directory = current_directory.parent
            for child in current_directory.children:
                if child.name == dir_name:
                    current_directory = child
        elif line.startswith('$ ls'):
            pass
        elif line.startswith('dir '):
            new_dir_name = line.split(' ')[1]
            # print('new dir ' + new_dir_name)
            new_dir = Directory(new_dir_name, current_directory)
            current_directory.add(new_dir)
        else:
            file_size, file_name = line.split(' ')
            # print(file_size, file_name)
            new_file = File(file_name, current_directory, int(file_size))
            current_directory.add(new_file)
        # print(f'Currently in dir {current_directory.name}')

    return root

def find_dirs_above_size(root, min_size):
    total_size = 0

    if hasattr(root, 'children'):
        for child in root.children:
            total_size += find_dirs_above_size(child, min_size)
    else:
        total_size += root.size

    # if total_size > min_size:
    #     total_size = 0
    return total_size

def find_dirs_above_size2(root, min_size):
    # total_size = 0

    if hasattr(root, 'children'):
        children_size = 0
        for child in root.children:
            children_size += find_dirs_above_size2(child, min_size)

    else:
        total_size += root.size

    # if total_size > min_size:
    #     total_size = 0
    return total_size

if __name__ == "__main__":

    input_filename = "example.txt"

    data = load_from_file(input_filename)

    # root = Directory('/', None)
    # dir = Directory('a', root)

    # root.add(dir)

    # file = File(name='a.txt', parent=dir)
    # dir.add(file)
    # file = File(name='b.txt', parent=dir)
    # dir.add(file)

    # print_tree(root)

    filesystem = parse_terminal_output(data)

    print_tree(filesystem)

    print(find_dirs_above_size(filesystem, 100000))