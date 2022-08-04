class Maze:
    def __init__(self, row: int, col: int):
        self.maze = []
        self.rowSize = 0
        self.colSize = 0
        for i in range(row):
            self.maze.append([])
            self.rowSize += 1
        for i in self.maze:
            for j in range(col):
                i.append('')
                self.colSize += 1
        self.colSize /= self.rowSize

    def in_bounds(self, row, col):
        return row < self.rowSize and col < self.colSize

    def is_marked(self, row, col):
        return self.maze[row][col] == '*'

    def is_open(self, row, col):
        return self.maze[row][col] == ''

    def is_tainted(self, row, col):
        return self.maze[row][col] == '^'

    def is_wall(self, row, col):
        return self.maze[row][col] == '-'

    def __str__(self):
        return str(self.maze)
