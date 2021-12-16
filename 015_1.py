class Solution:

    def __init__(self):
        self.cavern = []
        self.rows_number = 0
        self.cols_number = 0

    def read_input(self):
        input_file = open("input_015_0.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.cavern.append([int(v) for v in input_line])

        input_file.close()
        self.rows_number = len(self.cavern)
        self.cols_number = len(self.cavern[0])

    def calculate(self):
        return 0

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
