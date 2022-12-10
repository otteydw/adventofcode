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

    def add(self, child):
        self.children.append(child)

class File(Node):
    def __init__(self, name, parent, size=0):
        super().__init__(name, parent)

def tree(root, indent=0):
    print(' '*indent + '- ' + root.name)
    if hasattr(root, 'children'):
        for child in root.children:
            tree(child, indent+2)

if __name__ == "__main__":

    input_filename = "input.txt"

    data = load_from_file(input_filename)

    root = Directory('/', None)
    dir = Directory('a', root)

    root.add(dir)

    file = File(name='a.txt', parent=dir)
    dir.add(file)
    file = File(name='b.txt', parent=dir)
    dir.add(file)

    tree(root)