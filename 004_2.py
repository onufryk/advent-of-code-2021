import re


class Solution:

    def __init__(self):
        self.winning_boards = None
        self.winning_numbers = None
        self.randomized_numbers = None
        self.boards = None
        self.number_index = None
        self.board_rows = None
        self.board_cols = None
        self.board_numbers = None

    def read_input(self):
        self.randomized_numbers = None
        self.boards = []

        input_file = open("input_004_1.txt", "r")
        lineno = 0
        current_board_index = -1
        current_board = None
        for input_line in input_file:
            input_line = input_line.strip()
            if lineno == 0:
                self.randomized_numbers = [int(v) for v in input_line.strip().split(",")]
            else:
                if input_line == "":
                    if current_board:
                        self.boards.append(current_board)
                    current_board_index += 1
                    current_board = []
                else:
                    current_board.append([int(v) for v in re.split(r"\s+", input_line)])

            lineno += 1

        if current_board:
            self.boards.append(current_board)

        input_file.close()

    def precalculate(self):
        self.number_index = {}
        self.board_rows = {}
        self.board_cols = {}
        self.board_numbers = {}

        for board_index, board in enumerate(self.boards):
            self.board_numbers[board_index] = set()
            for row_index, row in enumerate(board):
                for col_index, number in enumerate(row):
                    if number not in self.number_index.keys():
                        self.number_index[number] = []
                    self.number_index[number].append((board_index, row_index, col_index))
                    self.board_numbers[board_index].add(number)
            self.board_rows[board_index] = [0] * len(board)
            self.board_cols[board_index] = [0] * len(board[0])

    def play(self):
        self.winning_boards = []
        self.winning_numbers = []
        for random_number in self.randomized_numbers:
            for b, r, c in self.number_index[random_number]:
                self.board_rows[b][r] += 1
                self.board_cols[b][c] += 1
                self.board_numbers[b].remove(random_number)
                if self.board_rows[b][r] == 5 or self.board_cols[b][c] == 5:
                    if b not in self.winning_boards:
                        self.winning_boards.append(b)
                        self.winning_numbers.append(random_number)
                if len(self.winning_boards) == len(self.boards):
                    return

    def solve(self):
        self.read_input()
        self.precalculate()
        self.play()
        return sum(self.board_numbers[self.winning_boards[-1]]) * self.winning_numbers[-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
