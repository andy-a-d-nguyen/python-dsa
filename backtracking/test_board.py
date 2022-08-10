from backtracking.board import Board


def test_board():
    b = Board(5)
    assert str(b) == str([
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', ''],
        ['', '', '', '', '']
    ])


def test_is_safe_vertically():
    b = Board(5)
    assert b.is_safe_vertically(3, 0) is True
    b.board[0][0] = '*'
    assert b.is_safe_vertically(3, 0) is False


def test_is_safe_horizontally():
    b = Board(5)
    assert b.is_safe_horizontally(0, 0) is True
    b.board[0][0] = '*'
    assert b.is_safe_horizontally(0, 3) is False


def test_is_safe_diagonally_from_left():
    b = Board(5)
    assert b.is_safe_diagonally_from_left(3, 3) is True
    b.board[0][0] = '*'
    assert b.is_safe_diagonally_from_left(3, 3) is False


def test_is_safe_diagonally_from_right():
    b = Board(5)
    assert b.is_safe_diagonally_from_right(3, 3) is True
    b.board[3][3] = '*'
    assert b.is_safe_diagonally_from_right(3, 3) is False


def test_is_safe():
    b = Board(5)
    assert b.is_safe(1, 1) is True
    b.board[1][1] = '*'
    assert b.is_safe(3, 3) is False


def test_place():
    b = Board(5)
    b.place(0, 0)
    assert b.is_safe(3, 3) is False
    assert b.is_safe(4, 1) is True


def test_remove():
    b = Board(5)
    b.place(0, 0)
    assert b.is_safe(3, 3) is False
    b.remove(0, 0)
    assert b.is_safe(3, 3) is True
