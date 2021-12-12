class Solution:

    def __init__(self):
        self.height_map = []

    def read_input(self):
        input_file = open("input_009_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.height_map.append([int(v) for v in list(input_line)])

        input_file.close()

    def calculate(self):
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
                    low_points.append(value)

        return sum([v+1 for v in low_points])

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
