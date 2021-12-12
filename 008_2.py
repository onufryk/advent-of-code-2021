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
        total = 0
        for i in range(len(self.inputs)):
            unique_digits = {
                2: 1,
                3: 7,
                4: 4,
                7: 8
            }
            digits = {
                0: None,
                1: None,
                2: None,
                3: None,
                4: None,
                5: None,
                6: None,
                7: None,
                8: None,
                9: None
            }
            segments = {
                'a': None,
                'b': None,
                'c': None,
                'd': None,
                'e': None,
                'f': None,
                'g': None
            }
            input = self.inputs[i]
            output = self.outputs[i]
            for pattern in input:
                if len(pattern) in unique_digits:
                    digits[unique_digits[len(pattern)]] = set(pattern)

            for pattern in output:
                if len(pattern) in unique_digits:
                    digits[unique_digits[len(pattern)]] = set(pattern)

            segments['a'] = set(digits[7]) - set(digits[1])
            segments['c'] = set(digits[1])
            segments['f'] = set(digits[1])
            segments['b'] = set(digits[4]) - set(digits[1])
            segments['d'] = set(digits[4]) - set(digits[1])
            segments['e'] = set(digits[8]) - set(digits[7]) - set(digits[4])
            segments['g'] = set(digits[8]) - set(digits[7]) - set(digits[4])

            # print(segments)
            for pattern in input + output:
                # print(pattern)
                if len(pattern) not in unique_digits:
                    pattern = set(pattern)

                    if len(segments['a'].intersection(pattern)) == 1:
                        # print("0. Segment A detected: 0, 2, 3, 5, 6, 9")
                        if len(segments['c'].intersection(pattern)) == 2 and len(segments['f'].intersection(pattern)) == 2 and len(segments['b'].intersection(pattern)) == 2 and len(segments['d'].intersection(pattern)) == 2:
                            # print("1. Segments BDCF detected: 9")
                            digits[9] = pattern
                            continue

                        if len(segments['b'].intersection(pattern)) == 2 and len(segments['d'].intersection(pattern)) == 2 and len(segments['e'].intersection(pattern)) == 2 and len(segments['g'].intersection(pattern)) == 2:
                            # print("1. Segments BDEG detected: 6")
                            digits[6] = pattern
                            continue

                        if len(segments['c'].intersection(pattern)) == 2 and len(segments['f'].intersection(pattern)) == 2 and len(segments['e'].intersection(pattern)) == 2 and len(segments['g'].intersection(pattern)) == 2:
                            # print("1. Segments CFEG detected: 0")
                            digits[0] = pattern
                            continue

                        if len(segments['b'].intersection(pattern)) == 2 and len(segments['d'].intersection(pattern)) == 2:
                            # print("1. Segments BD detected: 5, 6, 9")

                            if len(segments['e'].intersection(pattern)) == 1 and len(segments['c'].intersection(pattern)) == 1:
                                # print("2. SEG EC detected: 5")
                                digits[5] = pattern
                                continue

                        if len(segments['e'].intersection(pattern)) == 2 and len(segments['g'].intersection(pattern)) == 2:
                            # print("1. Segments EG detected: 0, 2, 6")

                            if len(segments['d'].intersection(pattern)) == 1 and len(segments['c'].intersection(pattern)) == 1:
                                # print("2. SEG DC detected: 2")
                                digits[2] = pattern
                                continue

                        if len(segments['c'].intersection(pattern)) == 2 and len(segments['f'].intersection(pattern)) == 2:
                            # print("1. Segments CF detected: 0, 3, 9")

                            if len(segments['d'].intersection(pattern)) == 1 and len(segments['g'].intersection(pattern)) == 1:
                                # print("2. SEG DG detected: 3")
                                digits[3] = pattern
                                continue

            output_value = []
            for pattern in output:
                # print("Pattern", set(pattern))
                for digit, digit_pattern in digits.items():
                    if digit_pattern == set(pattern):
                        output_value.append(digit)
            total += int("".join([str(val) for val in output_value]))
        return total


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
