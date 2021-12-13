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
        characters_mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'
        }
        score_mapping = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }

        error_score = 0
        for line in self.nav_subsys:
            print("Line: {}.".format(line), end=" ")
            stack = []
            is_corrupted = False
            for character in line:
                if character in opening_characters:
                    stack.append(character)
                if character in closing_characters:
                    if len(stack) == 0:
                        # print("Trying to close chunk on empty stack")
                        is_corrupted = True
                        error_score += score_mapping[character]
                        break

                    last_opening_character = stack[-1]

                    if last_opening_character != characters_mapping[character]:
                        # print("Trying to close chunk {} with {}".format(last_opening_character, character))
                        is_corrupted = True
                        error_score += score_mapping[character]
                        break

                    stack.pop()
            is_incomplete = len(stack) > 0
            if is_corrupted:
                print("Corrupted.")
            elif is_incomplete:
                print("Incomplete.")
            else:
                print(stack)
        return error_score


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
