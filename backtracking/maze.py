class Maze:
    def __init__(self, row: int, col: int):
        self.maze = []
        self.row = row
        self.col = col
        for i in range(row):
            self.maze.append([])
        for i in self.maze:
            for j in range(col):
                i.append('')
