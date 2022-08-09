class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        for i in range(size):
            self.board.append([])
            for j in range(size):
                self.board[i].append('')

    def in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size

    def is_safe(self, row, col):
        # base case
        # there's a queen where I'm placing
        if self.board[row][col] == '*':
            return False
        # recursive case
        # explore where I can go from where I am

    def is_safe_vertically(self, row, col):
        # Can't figure out why this causes stack overflow
        # if self.in_bounds(row, col) is False:
        #     return True
        # elif self.board[row][col] == '*':
        #     return False
        # else:
        #     return self.is_safe_vertically(row - 1, col) and self.is_safe_vertically(row + 1, col)
        upper_limit = row
        lower_limit = row
        while upper_limit >= 0:
            if self.board[upper_limit][col] == '*':
                return False
            upper_limit -= 1
        while lower_limit < self.size:
            if self.board[lower_limit][col] == '*':
                return False
            lower_limit += 1
        return True

    def is_safe_horizontally(self, row, col):
        left_limit = col
        right_limit = col
        while left_limit >= 0:
            if self.board[row][left_limit] == '*':
                return False
            left_limit -= 1
        while right_limit < self.size:
            if self.board[row][right_limit] == '*':
                return False
            right_limit += 1
        return True

    def __str__(self):
        return str(self.board)
