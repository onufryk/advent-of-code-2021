import collections
import copy


class Solution:

    def __init__(self):
        self.template = None
        self.insertion_rules = {}
        self.frequency = collections.defaultdict(int)

    def read_input(self):
        input_file = open("input_014_0.txt", "r")
        i = 0
        for input_line in input_file:
            input_line = input_line.strip()
            if i == 0:
                self.template = input_line
            elif input_line != "":
                insertion_rule = input_line.split(" -> ")
                self.insertion_rules[insertion_rule[0]] = insertion_rule[1]

            i += 1

        input_file.close()

    def calculate(self):
        return 0


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print("Solution: {}".format(solution.solve()))
