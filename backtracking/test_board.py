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
