import collections
import time


class Solution:

    def __init__(self):
        self.template = None
        self.insertion_rules = {}
        self.pairs_frequency = collections.defaultdict(int)

    def read_input(self):
        input_file = open("input_014_1.txt", "r")
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
        for i in range(len(self.template) - 1):
            pair = self.template[i:i + 2]
            self.pairs_frequency[pair] += 1

        for step_number in range(1, 41):
            add_pairs = []
            delete_pairs = []
            for pair, amount in self.pairs_frequency.items():
                if amount == 0:
                    continue
                add_pairs.append((pair[0] + self.insertion_rules[pair], amount))
                add_pairs.append((self.insertion_rules[pair] + pair[1], amount))
                delete_pairs.append((pair, amount))
            print("Add:    {}".format(add_pairs))
            print("Delete: {}".format(delete_pairs))
            for pair, amount in delete_pairs:
                self.pairs_frequency[pair] -= amount
            for pair, amount in add_pairs:
                self.pairs_frequency[pair] += amount

        print("Pairs frequency: {}".format(self.pairs_frequency))
        for polymer in sorted(self.pairs_frequency.keys()):
            print("{}: {}".format(polymer, self.pairs_frequency[polymer]))

        letter_frequency = collections.defaultdict(int)
        letter_frequency[self.template[0]] += 1
        letter_frequency[self.template[-1]] += 1
        for pair, amount in self.pairs_frequency.items():
            letter_frequency[pair[0]] += amount
            letter_frequency[pair[1]] += amount
        for letter in letter_frequency.keys():
            letter_frequency[letter] //= 2

        print("Frequency:")
        for polymer in sorted(letter_frequency.keys()):
            print("{}: {}".format(polymer, letter_frequency[polymer]))

        return max([v for k, v in letter_frequency.items()]) - min([v for k, v in letter_frequency.items()])

    def solve(self):
        self.read_input()
        start = time.time_ns()
        calculate = self.calculate()
        end = time.time_ns() - start
        print(end)


if __name__ == "__main__":
    solution = Solution()
    print("Solution: {}".format(solution.solve()))
