class Solution:

    def __init__(self):
        self.nav_subsys = []

    def read_input(self):
        input_file = open("input_010_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.nav_subsys.append(input_line)

        input_file.close()

    def calculate(self):
        opening_characters = {'(', '[', '{', '<'}
        closing_characters = {')', ']', '}', '>'}
        opening_characters_mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
        }
        closing_characters_mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }
        score_mapping = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }

        closing_scores = []
        for line in self.nav_subsys:
            print("Line: {}.".format(line), end=" ")
            stack = []
            is_corrupted = False
            for character in line:
                if character in opening_characters:
                    stack.append(character)
                if character in closing_characters:
                    if len(stack) == 0:
                        is_corrupted = True
                        break

                    last_opening_character = stack[-1]

                    if last_opening_character != opening_characters_mapping[character]:
                        is_corrupted = True
                        break

                    stack.pop()

            is_incomplete = len(stack) > 0

            if is_corrupted:
                print("- Corrupted. Skip.")
            elif is_incomplete:
                closing_sequence = []
                closing_score = 0
                while len(stack) > 0:
                    character = stack.pop()
                    closing_sequence.append(closing_characters_mapping[character])
                    closing_score = closing_score * 5 + score_mapping[closing_characters_mapping[character]]
                print(" - Complete by adding {}, score {}.".format("".join(closing_sequence), closing_score))
                closing_scores.append(closing_score)
            else:
                print()

        return sorted(closing_scores)[len(closing_scores)//2]


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
