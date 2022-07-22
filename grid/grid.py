class Grid:
    def __init__(self, rows=0, columns=0):
        self.grid = []
        if rows > 0:
            i = 0
            while i < rows:
                self.grid.append([])
                i += 1
        if columns > 0:
            for index, _ in enumerate(self.grid):
                j = 0
                while j < columns:
                    self.grid[index].append("")
                    j += 1

    def get(self, row, column):
        if self.num_rows() >= row and self.num_cols() >= column:
            return self.grid[row][column]
        else:
            return None

    def fill(self, value):
        for row in self.grid:
            for i in range(len(row)):
                row[i] = value

    def in_bounds(self, row_index, column_index):
        if row_index < len(self.grid) and column_index < len(self.grid[0]):
            return True
        else:
            return False

    def num_cols(self):
        return len(self.grid[0])

    def num_rows(self):
        return len(self.grid)

    def resize(self, rows, columns):
        self.__init__(rows, columns)

    def set(self, row, column, value):
        self.grid[row][column] = value

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return str(self.grid)


def knight_can_move(
        grid: Grid,
        row1: int,
        column1: int,
        row2: int,
        column2: int
):
    if grid.in_bounds(row1, column1) is False or grid.in_bounds(row2, column2) is False:
        return False
    if grid.get(row1, column1) != "knight" or grid.get(row2, column2) is None:
        return False
    row_distance = abs(row1 - row2)
    column_distance = abs(column1 - column2)
    if (row_distance == 1 and column_distance != 2) or (row_distance == 2 and column_distance != 1):
        return False
    return True
