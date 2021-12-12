import re


class Solution:

    def __init__(self):
        self.lines = []
        self.max_x = 0
        self.max_y = 0

    def read_input(self):
        input_file = open("input_005_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            start, end = input_line.split(" -> ")
            start = [int(v) for v in start.split(",")]
            end = [int(v) for v in end.split(",")]
            dir = 0
            if start[0] == end[0]:
                dir = 0
            elif start[1] == end[1]:
                dir = 1
            else:
                dir = -1
            if start[1] > end[1] or start[0] > end[0]:
                self.lines.append((end, start, dir))
            else:
                self.lines.append((start, end, dir))

            if start[0] > self.max_x:
                self.max_x = start[0]
            if end[0] > self.max_x:
                self.max_x = end[0]
            if start[1] > self.max_y:
                self.max_y = start[1]
            if end[1] > self.max_y:
                self.max_y = end[1]

        input_file.close()
        print(self.lines)

    def calculate(self):
        count = 0

        matrix = [0] * (self.max_x + 1)
        for i in range(len(matrix)):
            matrix[i] = [0] * (self.max_y + 1)

        for line in self.lines:

            start_i, end_i, dir_i = line  # x1, y1, x2, y2
            if dir_i == 1:
                for j in range(start_i[0], end_i[0]+1):
                    matrix[start_i[1]][j] += 1

            elif dir_i == 0:
                for j in range(start_i[1], end_i[1]+1):
                    matrix[j][start_i[0]] += 1
            else:
                if start_i[0] < end_i[0] and start_i[1] < end_i[1]:
                    for i in range(end_i[0] - start_i[0] + 1):
                        matrix[start_i[1] + i][start_i[0] + i] += 1
                else:
                    if start_i[0] <= end_i[0]:
                        for i in range(end_i[0] - start_i[0] + 1):
                            matrix[start_i[1]-i][start_i[0]+i] += 1
                    else:
                        for i in range(start_i[0] - end_i[0] + 1):
                            matrix[start_i[1]+i][start_i[0]-i] += 1


        for row in matrix:
            print(row)
            for value in row:
                if value > 1:
                    count += 1


        return count

    def calculate_1(self):
        count = 0
        for i in range(len(self.lines) - 1):
            for j in range(i + 1, len(self.lines)):
                start_i, end_i, dir_i = self.lines[i]  # x1, y1, x2, y2
                start_j, end_j, dir_j = self.lines[j]  # x3, y3, x4, y4
                print("Lines {} - {} ({}) and {} - {} ({}).".format(start_i, end_i, 'H' if dir_i else 'V', start_j, end_j, 'H' if dir_j else 'V'))

                x1 = start_i[0]
                y1 = start_i[1]
                x2 = end_i[0]
                y2 = end_i[1]
                x3 = start_j[0]
                y3 = start_j[1]
                x4 = end_j[0]
                y4 = end_j[1]

                denominator = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

                if denominator == 0:
                    if x1 == x3:
                        if y3 <= y1 <= y4 or y3 <= y1 <= y4 or y1 <= y3 <= y2 or y1 <= y4 <= y2:
                            count += min(x2, x4) - max(x1, x3) + 1
                    elif y1 == y3:
                        if x3 <= x1 <= x4 or x2 <= x1 <= x4 or x1 <= x3 <= x2 or x1 <= x4 <= x2:
                            count += min(y2, y4) - max(y1, y3) + 1
                else:
                    px = int(((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator)
                    py = int(((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator)

                    if x1 <= px <= x2 and x3 <= px <= x4 and y1 <= py <= y2 and y3 <= py <= y4:
                        count += 1
            print()
        return count


    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
