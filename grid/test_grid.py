from grid.grid import Grid
from grid.grid import knight_can_move


def test_grid():
    grid = Grid(1, 3)
    assert len(grid.grid) == 1
    for row in grid.grid:
        assert len(row) == 3


def test_get():
    grid = Grid(1, 3)
    assert grid.grid[0][2] == ""
    assert grid.get(0, 1) == ""


def test_fill():
    grid = Grid(2, 3)
    assert str(grid) == str([
        ["", "", ""],
        ["", "", ""]
    ])
    grid.fill(3)
    assert str(grid) == str([
        [3, 3, 3],
        [3, 3, 3]
    ])


def test_in_bounds():
    grid = Grid(3, 3)
    assert grid.in_bounds(2, 2) is True
    assert grid.in_bounds(4, 3) is False
    assert grid.in_bounds(3, 4) is False


def test_num_cols():
    grid = Grid(3, 3)
    assert grid.num_cols() == 3


def test_num_rows():
    grid = Grid(3, 3)
    assert grid.num_rows() == 3


def test_resize():
    grid = Grid(3, 3)
    grid.resize(2, 2)
    assert grid.num_rows() == 2
    assert grid.num_cols() == 2


def test_set():
    grid = Grid(2, 2)
    grid.set(1, 1, 2)
    assert grid.get(1, 1) == 2


def test_to_string():
    grid = Grid(2, 2)
    assert grid.to_string() == str([
        ["", ""],
        ["", ""]
    ])


def test_knight_can_move():
    board = Grid(3, 3)
    assert knight_can_move(board, 4, 4, 2, 3) is False
    assert knight_can_move(board, 1, 2, 2, 4) is False
    board.set(0, 0, "knight")
    assert knight_can_move(board, 0, 0, 1, 2) is True
