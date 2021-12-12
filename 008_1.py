class Solution:

    def __init__(self):
        self.inputs = []
        self.outputs = []

    def read_input(self):
        input_file = open("input_008_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            input, output = input_line.split(" | ")
            self.inputs.append(input.split(" "))
            self.outputs.append(output.split(" "))

        input_file.close()

    def calculate(self):
        count = 0
        for combination in self.outputs:
            for signal in combination:
                if len(signal) in [2, 3, 4, 7]:
                    count += 1
        return count

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
