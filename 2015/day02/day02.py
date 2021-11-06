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

    def smallest_perimeter(self):
        dimensions = [self.length, self.width, self.height]
        dimensions.sort()
        smallest_perimeter = 2 * dimensions[0] + 2 * dimensions[1]
        return smallest_perimeter

    def volume(self):
        return self.length * self.width * self.height

    def ribbon_needed(self):
        return self.smallest_perimeter() + self.volume()

if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    total_paper = 0
    total_ribbon = 0

    with open(input_path) as input_file:
        for line in input_file:
            dimension = line.rstrip()
            present = Present(dimension)
            total_paper += present.paper_needed()
            total_ribbon += present.ribbon_needed()

    print(f"Paper: {total_paper}")
    print(f"Ribbon: {total_ribbon}")