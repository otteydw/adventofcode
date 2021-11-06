import os

class Present():
    def __init__(self, dimensions):
        self.length, self.width, self.height = [int(x) for x in dimensions.split("x")]

    def surface_area(self):
        surface_area = 2*self.length*self.width + 2*self.width*self.height + 2*self.height*self.length
        return surface_area

    def smallest_side_area(self):
        smallest_side_area = min(self.length*self.width, self.width*self.height, self.height*self.length)
        return smallest_side_area

    def paper_needed(self):
        return self.surface_area() + self.smallest_side_area()

if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    total_paper = 0

    with open(input_path) as input_file:
        for line in input_file:
            dimension = line.rstrip()
            present = Present(dimension)
            total_paper += present.paper_needed()

    print(total_paper)