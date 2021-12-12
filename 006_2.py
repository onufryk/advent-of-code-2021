import copy
import re


class Solution:

    def __init__(self):
        self.count = 0
        self.groups = [None] * 9
        for i in range(len(self.groups)):
            self.groups[i] = 0

    def read_input(self):
        input_file = open("input_006_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            school = [int(v) for v in input_line.split(",")]
            self.count = len(school)
            for index, fish in enumerate(school):
                self.groups[fish] += 1

        input_file.close()

    def calculate(self):
        for day in range(256):
            self.rotate()
        return self.count

    def rotate(self):
        group_0 = copy.copy(self.groups[0])
        self.groups[0] = self.groups[1]
        self.groups[1] = self.groups[2]
        self.groups[2] = self.groups[3]
        self.groups[3] = self.groups[4]
        self.groups[4] = self.groups[5]
        self.groups[5] = self.groups[6]
        self.groups[6] = self.groups[7] + group_0
        self.groups[7] = self.groups[8]
        self.groups[8] = group_0
        self.count += group_0

    def print_groups(self):
        for timer, fishes in enumerate(self.groups):
            print("Timer {} has fish {}".format(timer, fishes))

    def print_groups2(self):
        for timer, fishes in enumerate(self.groups_2):
            print("Timer {} has {} fish".format(timer, fishes))

    def print_school(self):
        output = ['0'] * self.count
        for timer, fishes in enumerate(self.groups):
            for fish in fishes:
                output[fish] = str(timer)
        print(output)
        return ",".join(output)

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
