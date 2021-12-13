import copy


class Solution:

    def __init__(self):
        self.cavern = []

    def read_input(self):
        input_file = open("input_011_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.cavern.append([int(v) for v in list(input_line)])

        input_file.close()

    def increment(self):
        n = len(self.cavern)
        m = len(self.cavern[0])
        for i in range(n):
            for j in range(m):
                self.cavern[i][j] += 1

    def expand_flash(self, i, j, flashed):
        n = len(self.cavern)
        m = len(self.cavern[0])

        # directions = [(-1, 0), (+1, 0), ]

        if (i - 1) >= 0:
            if not flashed[i - 1][j]:
                self.cavern[i - 1][j] += 1
        if (i + 1) < n:
            if not flashed[i + 1][j]:
                self.cavern[i + 1][j] += 1
        if (j - 1) >= 0:
            if not flashed[i][j - 1]:
                self.cavern[i][j - 1] += 1
        if (j + 1) < m:
            if not flashed[i][j + 1]:
                self.cavern[i][j + 1] += 1
        if (i - 1) >= 0 and (j - 1) >= 0:
            if not flashed[i - 1][j - 1]:
                self.cavern[i - 1][j - 1] += 1
        if (i - 1) >= 0 and (j + 1) < m:
            if not flashed[i - 1][j + 1]:
                self.cavern[i - 1][j + 1] += 1
        if (i + 1) < n and (j - 1) >= 0:
            if not flashed[i + 1][j - 1]:
                self.cavern[i + 1][j - 1] += 1
        if (i + 1) < n and (j + 1) < m:
            if not flashed[i + 1][j + 1]:
                self.cavern[i + 1][j + 1] += 1

    def step(self):
        n = len(self.cavern)
        m = len(self.cavern[0])

        flashed = [None] * n
        for i in range(n):
            flashed[i] = [False] * m

        is_dirty = True
        flashes_count = 0

        while is_dirty:
            is_dirty = False
            for i in range(n):
                for j in range(m):
                    if self.cavern[i][j] > 9:
                        flashed[i][j] = True
                        flashes_count += 1
                        self.cavern[i][j] = 0
                        is_dirty = True

                        self.expand_flash(i, j, flashed)

        return flashes_count

    def calculate(self):
        n = len(self.cavern)
        m = len(self.cavern[0])

        # print("Before any steps:")
        # self.print_cavern(self.cavern)
        flashes_count = 0
        step_number = 0

        while flashes_count != n * m:
            self.increment()
            flashes_count = self.step()

            # print("Flashes after step {}: {}".format(step_number + 1, flashes_count))
            # print("After step {}:".format(step_number + 1))
            # self.print_cavern(self.cavern)
            step_number += 1

        return step_number

    @staticmethod
    def print_cavern(cavern):
        for row in cavern:
            for value in row:
                if value == 0:
                    print(value, end=' ')
                else:
                    print(value, end=' ')
            print()

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
