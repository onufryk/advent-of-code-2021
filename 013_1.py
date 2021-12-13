import re

class Solution:

    def __init__(self):
        self.max_x = 0
        self.max_y = 0
        self.points = []
        self.commands = []
        self.map = None

    def read_input(self):
        input_file = open("input_013_1.txt", "r")
        mode = "points"
        command_pattern = re.compile(r"fold along (\w)=(\d+)")
        for input_line in input_file:
            input_line = input_line.strip()
            if input_line == "":
                mode = "commands"
                continue
            if mode == "points":
                coords = [int(a) for a in input_line.split(",")]
                x = coords[1]
                y = coords[0]
                self.max_x = max(self.max_x, x)
                self.max_y = max(self.max_y, y)
                self.points.append((x, y))
            elif mode == "commands":
                result = command_pattern.match(input_line)
                self.commands.append((result.group(1), int(result.group(2))))

        input_file.close()

    def print_map(self):
        # print()
        self.map = [None] * self.max_x
        for i in range(self.max_x):
            self.map[i] = [' '] * self.max_y

        for x, y in self.points:
            self.map[x][y] = '#'

        for axis, argument in self.commands:
            if axis == "y":
                for y in range(self.max_y):
                    self.map[argument][y] = '-'
            elif axis == "x":
                for x in range(self.max_x):
                    self.map[x][argument] = '|'

        # for row in self.map:
        #     print(''.join(row))

    def print_visible_map(self):
        max_x = 0
        max_y = 0
        for x, y in self.points:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        max_x += 1
        max_y += 1

        map = [None] * max_x
        for i in range(max_x):
            map[i] = [' '] * max_y

        for x, y in self.points:
            map[x][y] = '#'

        for row in map:
            print(''.join(row))


    def process_command(self, axis, argument):
        if axis == "y":
            for i, coords in enumerate(self.points):
                x, y = coords
                if x < argument:
                    continue
                self.points[i] = (argument - (x - argument), y)
        elif axis == "x":
            for i, coords in enumerate(self.points):
                x, y = coords
                if y < argument:
                    continue
                self.points[i] = (x, argument - (y - argument))

    def count_visible(self):
        visible = 0
        for row in self.map:
            visible += sum([v == "#" for v in row])
        return visible

    def calculate(self):
        self.max_y += 1
        self.max_x += 1

        self.print_map()

        for axis, argument in self.commands:
            self.process_command(axis, argument)

        self.print_map()
        self.print_visible_map()
        return self.count_visible()


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
