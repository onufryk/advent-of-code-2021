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

    def expand(self, pair, level):
        print("{}. {}".format(level, pair))
        new_pair = [self.insertion_rules[''.join(pair)], pair[-1]]
        print("New  pair {}".format(new_pair))

    def count(self, sequence):
        if len(sequence) < 2:
            return
        print("{}".format(sequence))
        prefix = sequence[:-1]
        last_pair = sequence[-2:]
        print("Prefix {}".format(prefix))
        print("Last pair {}".format(last_pair))

        self.expand(last_pair, 0)

        self.count(sequence[:-1])

    def calculate(self):
        current_template = list(self.template)

        self.count(current_template)

        # for i in range(5):
        #     print("Template:      {}".format(current_template))
        #     prefix = current_template[:-1]
        #     last_pair = current_template[-2:]
        #     print("Prefix {}".format(prefix))
        #     print("Last pair {}".format(last_pair))
        #
        #     current_template.pop()
        #     current_template += new_pair


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print("Solution: {}".format(solution.solve()))
