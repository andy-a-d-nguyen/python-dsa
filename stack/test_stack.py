import pytest

from stack.stack import Stack
from stack.stack import check_balance


def test_stack():
    s = Stack()
    assert str(s) == str([])


def test_is_empty():
    s = Stack()
    assert s.is_empty() is True


def test_peek():
    s = Stack()
    with pytest.raises(Exception) as message:
        s.peek()
    assert message.value.args[0] == 'List is empty'
    s.stack.append(1)
    assert s.peek() == 1


def test_pop():
    s = Stack()
    with pytest.raises(Exception) as message:
        s.pop()
    assert message.value.args[0] == 'List is empty'
    s.stack.append(1)
    assert s.pop() == 1


def test_push():
    s = Stack()
    s.push(1)
    assert str(s) == str([1])


def test_size():
    s = Stack()
    assert s.size() == 0


def test_check_balance():
    assert check_balance('if (a(4) > 9) { foo(a(2)); }') == -1
    assert check_balance('for (i=0;i<a(3};i++) {foo{); )') == 14
    assert check_balance('while (true) foo(); }{ ()') == 20
    assert check_balance('if (x) {') == 8

