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
        return 0 <= row < self.rowSize and 0 <= col < self.colSize

    def is_marked(self, row, col):
        if self.in_bounds(row, col):
            return self.maze[row][col] == '*'

    def is_open(self, row, col):
        return self.maze[row][col] == ''

    def is_tainted(self, row, col):
        return self.maze[row][col] == 'x'

    def is_wall(self, row, col):
        return self.maze[row][col] == '-'

    def mark(self, row, col):
        self.maze[row][col] = '*'

    def taint(self, row, col):
        self.maze[row][col] = 'x'

    def unmark(self, row, col):
        if self.is_marked(row, col):
            self.maze[row][col] = ''

    def un_taint(self, row, col):
        if self.is_tainted(row, col):
            self.maze[row][col] = ''

    def __str__(self):
        return str(self.maze)


'''
Write a function escape_maze(maze, row, col) that searches
for a path out of a given 2-dimensional maze
- Return true if able to scape, or false if not
- 'Escaping' means exiting the maze boundaries
- You can move 1 square at a time in any of the 4 directions
- 'Mark' your path along the way
- 'Taint' bad paths that do not work
- Do not explore the same path twice
'''


def escape_maze(maze: Maze, row: int, col: int) -> bool:
    # base case
    if maze.in_bounds(row, col) is False:
        return True
    elif maze.is_wall(row, col) is True:
        return False
    elif maze.is_open(row, col):
        # choose
        maze.mark(row, col)

        # explore
        result = (escape_maze(maze, row - 1, col)
                  or escape_maze(maze, row + 1, col)
                  or escape_maze(maze, row, col - 1)
                  or escape_maze(maze, row, col + 1))

        # un-choose
        if result is False:
            maze.taint(row, col)

        return result
    else:
        return False


def escape_maze_alternative(maze: Maze, row: int, col: int) -> bool:
    if maze.in_bounds(row, col) is False:
        # base case 1: escaped
        return True
    elif maze.is_open(row, col) is False:
        # base case 2: blocked
        return False
    else:
        # recursive case: try to escape in 4 directions
        maze.mark(row, col)
        if (escape_maze_alternative(maze, row - 1, col)
                or escape_maze_alternative(maze, row + 1, col)
                or escape_maze_alternative(maze, row, col - 1)
                or escape_maze_alternative(maze, row, col + 1)):
            # one of the paths worked
            return True
        else:
            maze.taint(row, col)
            # all 4 paths failed; taint
            return False


def escape_maze_arms_length(maze: Maze, row: int, col: int) -> bool:
    maze.mark(row, col)

    # recursive case: try to escape in 4 directions
    # check each one by arm's length
    if maze.in_bounds(row - 1, col) and maze.is_open(row - 1, col):
        if escape_maze_arms_length(maze, row - 1, col):
            return True
    if maze.in_bounds(row + 1, col) and maze.is_open(row + 1, col):
        if escape_maze_arms_length(maze, row + 1, col):
            return True
    if maze.in_bounds(row, col - 1) and maze.is_open(row, col - 1):
        if escape_maze_arms_length(maze, row, col - 1):
            return True
    if maze.in_bounds(row, col + 1) and maze.is_open(row, col + 1):
        if escape_maze_alternative(maze, row, col + 1):
            return True

    maze.taint(row, col)
    # all 4 paths failed; taint
    return False
