class Solution:

    def __init__(self):
        self.positions = []

    def read_input(self):
        input_file = open("input_007_1.txt", "r")
        for input_line in input_file:
            input_line = input_line.strip()
            self.positions = [int(v) for v in input_line.split(',')]

        input_file.close()

    def calculate(self):
        costs = [-1] * (max(self.positions) + 1)
        for position in range(0, max(self.positions) + 1):
            costs[position] = self.calculate_for_position(position)
        # print(costs)
        return min(costs)

    def calculate_for_position(self, pos):
        # print("Calculating for pos {} ".format(pos))
        cost = 0
        for position in self.positions:
            diff = abs(position - pos)
            c = diff * (diff + 1) // 2
            # print("Move from {} to {}: {} fuel".format(position, pos, c))
            cost += c
        return cost

    def solve(self):
        self.read_input()
        return self.calculate()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
