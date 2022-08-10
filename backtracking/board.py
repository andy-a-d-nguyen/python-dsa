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

    def is_safe_diagonally_from_left(self, row, col):
        left_upper_limit = [row, col]
        right_lower_limit = [row, col]
        while left_upper_limit[0] >= 0 and left_upper_limit[1] >= 0:
            if self.board[left_upper_limit[0]][left_upper_limit[1]] == '*':
                return False
            left_upper_limit[0] -= 1
            left_upper_limit[1] -= 1
        while right_lower_limit[0] < self.size and right_lower_limit[1] < self.size:
            if self.board[right_lower_limit[0]][right_lower_limit[1]] == '*':
                return False
            right_lower_limit[0] += 1
            right_lower_limit[1] += 1
        return True

    def is_safe_diagonally_from_right(self, row, col):
        left_lower_limit = [row, col]
        right_upper_limit = [row, col]
        while left_lower_limit[0] < self.size and left_lower_limit[1] >= 0:
            if self.board[left_lower_limit[0]][left_lower_limit[1]] == '*':
                return False
            left_lower_limit[0] += 1
            left_lower_limit[1] -= 1
        while right_upper_limit[0] >= 0 and right_upper_limit[1] < self.size:
            if self.board[right_upper_limit[0]][right_upper_limit[1]] == '*':
                return False
            right_upper_limit[0] -= 1
            right_upper_limit[1] += 1
        return True

    def is_safe(self, row, col):
        if (self.is_safe_horizontally(row, col)
                and self.is_safe_vertically(row, col)
                and self.is_safe_diagonally_from_left(row, col)
                and self.is_safe_diagonally_from_right(row, col)):
            return True
        else:
            return False

    def __str__(self):
        return str(self.board)
