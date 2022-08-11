import pytest

from classes_and_objects.array_stack import ArrayStack


def test_array_stack():
    array_stack = ArrayStack()
    assert len(array_stack.elements) == 10
    assert array_stack.size == 0
    assert array_stack.capacity == 10


def test_push():
    array_stack = ArrayStack()
    array_stack.push(1)
    assert array_stack.size == 1
    assert array_stack.peek() == 1
    array_stack.push(2)
    array_stack.push(3)
    array_stack.push(4)
    array_stack.push(5)
    array_stack.push(6)
    array_stack.push(7)
    array_stack.push(8)
    array_stack.push(9)
    array_stack.push(10)
    array_stack.push(11)
    assert array_stack.peek() == 11
    assert array_stack.size == 11


def test_pop():
    array_stack = ArrayStack()
    array_stack.push(1)
    assert array_stack.pop() == 1
    assert array_stack.size == 0
    with pytest.raises(IndexError) as error:
        array_stack.pop()
    assert error.value.args[0] == 'List is empty'
    assert array_stack.size == 0


def test_peek():
    array_stack = ArrayStack()
    with pytest.raises(IndexError) as error:
        array_stack.peek()
    assert error.value.args[0] == 'List is empty'
    array_stack.push(1)
    assert array_stack.peek() == 1
    assert array_stack.size == 1


def test_is_empty():
    array_stack = ArrayStack()
    assert array_stack.is_empty() is True


def test_to_string():
    array_stack = ArrayStack()
    array_stack.push(1)
    assert array_stack.to_string() == str([1])
    array_stack.pop()
    assert array_stack.capacity == 5
    assert array_stack.size == 0
