import collections

class Solution:

    def __init__(self):
        self.template = None
        self.insertion_rules = {}

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
        print("Template:      {}".format(self.template))

        for step_number in range(1, 41):
            new_template = []
            for i in range(len(self.template)-1):
                new_template.append(self.template[i])
                new_template.append(self.insertion_rules[self.template[i] + self.template[i+1]])
            new_template.append(self.template[-1])
            self.template = ''.join(new_template)
            print("After step {:2}: {}".format(step_number, self.template if len(self.template) < 97 else len(self.template)))

        pairs = collections.defaultdict(int)
        for i in range(len(self.template)-1):
            pairs[self.template[i:i+2]] += 1
        print("Pairs:      {}".format(pairs))

        frequency = collections.Counter(self.template)
        print("Frequency:")
        for polymer in sorted(frequency.keys()):
            print("{}: {}".format(polymer, frequency[polymer]))
        return max([v for k,v in frequency.items()]) - min([v for k,v in frequency.items()])

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print("Solution: {}".format(solution.solve()))
