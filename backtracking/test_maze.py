from backtracking.maze import Maze


def test_maze():
    m = Maze(3, 3)
    assert str(m) == str([
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ])
    assert m.colSize == 3
    assert m.rowSize == 3
    m = Maze(3, 4)
    assert str(m) == str([
        ['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
    ])
    assert m.colSize == 4
    assert m.rowSize == 3


def test_in_bounds():
    m = Maze(3, 3)
    assert m.in_bounds(2, 2) is True
    assert m.in_bounds(3, 3) is False
    assert m.in_bounds(0, 0) is True
    assert m.in_bounds(0, -2) is False


def test_is_marked():
    m = Maze(3, 3)
    m.maze[0][0] = '*'
    assert m.is_marked(0, 0) is True
    assert m.is_marked(0, 1) is False


def test_is_open():
    m = Maze(3, 3)
    m.maze[0][0] = '*'
    assert m.is_open(0, 0) is False
    assert m.is_open(0, 1) is True


def test_is_tainted():
    m = Maze(3, 3)
    m.maze[0][0] = '^'
    assert m.is_tainted(0, 0) is True
    assert m.is_tainted(2, 2) is False


def test_is_wall():
    m = Maze(3, 3)
    m.maze[0][0] = '-'
    assert m.is_wall(0, 0) is True
    assert m.is_wall(0, 1) is False


def test_mark():
    m = Maze(3, 3)
    m.mark(0, 0)
    assert m.is_marked(0, 0) is True


def test_taint():
    m = Maze(3, 3)
    m.taint(0, 0)
    assert m.is_tainted(0, 0) is True


def test_unmark():
    m = Maze(3, 3)
    m.mark(0, 0)
    m.unmark(0, 0)
    assert m.is_marked(0, 0) is False


def test_un_taint():
    m = Maze(3, 3)
    m.taint(0, 0)
    m.un_taint(0, 0)
    assert m.is_tainted(0, 0) is False
