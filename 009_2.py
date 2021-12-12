import functools
import itertools

class Solution:

    def __init__(self):
        self.height_map = []

    def read_input(self):
        input_file = open("input_009_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.height_map.append([int(v) for v in list(input_line)])

        input_file.close()

    def find_low_points(self):
        low_points = []
        for i, row in enumerate(self.height_map):
            for j, value in enumerate(row):
                adj_values = []

                if i - 1 >= 0:
                    adj_values.append(self.height_map[i - 1][j])

                if i + 1 < len(self.height_map):
                    adj_values.append(self.height_map[i + 1][j])
                if j - 1 >= 0:
                    adj_values.append(self.height_map[i][j - 1])

                if j + 1 < len(row):
                    adj_values.append(self.height_map[i][j + 1])

                if min(adj_values) > value:
                    low_points.append((i, j, value))
        return low_points

    def explore_basin(self, point, visited, level=1):
        if point in visited:
            return 0

        # print("{}. Explore {}".format(level, point))

        i = point[0]
        j = point[1]

        if self.height_map[i][j] == 9:
            # print("Size 0")
            return 0

        size = 1
        visited.add(point)

        if i - 1 >= 0:
            size += self.explore_basin((i - 1, j, self.height_map[i - 1][j]), visited, level + 1)

        if i + 1 < len(self.height_map):
            size += self.explore_basin((i + 1, j, self.height_map[i + 1][j]), visited, level + 1)

        if j - 1 >= 0:
            size += self.explore_basin((i, j - 1, self.height_map[i][j - 1]), visited, level + 1)

        if j + 1 < len(self.height_map[0]):
            size += self.explore_basin((i, j + 1, self.height_map[i][j + 1]), visited, level + 1)

        # print("Size {}".format(size))

        return size

    def calculate(self):
        low_points = self.find_low_points()
        basins = []
        for low_point in low_points:
            basins.append(self.explore_basin(low_point, set()))

        print(list(itertools.accumulate(sorted(basins, reverse=True)[:3], func=lambda x,y: x * y, initial=1)))

        return functools.reduce(lambda x,y: x * y, sorted(basins, reverse=True)[:3])

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
