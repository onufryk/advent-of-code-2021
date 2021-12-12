import copy
import re


class Solution:

    def __init__(self):
        self.count = 0
        self.groups = [None] * 9
        for i in range(len(self.groups)):
            self.groups[i] = []

    def read_input(self):
        input_file = open("input_006_0.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            school = [int(v) for v in input_line.split(",")]
            self.count = len(school)
            for index, fish in enumerate(school):
                self.groups[fish].append(index)

        input_file.close()

    def calculate(self):
        print("Initial state: {}".format(self.print_school()))
        for day in range(80):
            self.rotate(day)
        return self.count

    def rotate(self, day):
        group_0 = copy.copy(self.groups[0])
        self.groups[0] = self.groups[1]
        self.groups[1] = self.groups[2]
        self.groups[2] = self.groups[3]
        self.groups[3] = self.groups[4]
        self.groups[4] = self.groups[5]
        self.groups[5] = self.groups[6]
        self.groups[6] = self.groups[7] + group_0
        self.groups[7] = self.groups[8]
        self.groups[8] = []
        for parent in group_0:
            self.groups[8].append(self.count)
            self.count += 1
        print("After  {} days: {}".format(day+1, self.print_school()))
        # self.print_groups()

    def print_groups(self):
        for timer, fishes in enumerate(self.groups):
            print("Timer {} has fish {}".format(timer, fishes))

    def print_school(self):
        output = [0] * self.count
        for timer, fishes in enumerate(self.groups):
            for fish in fishes:
                output[fish] = str(timer)
        return ",".join(output)

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
