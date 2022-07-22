from vector.vector import Vector
from vector.vector import count_in_range
from vector.vector import remove_all


def test_vector():
    vector = Vector()
    assert str(vector) == str([])


def test_add():
    vector = Vector()
    vector.add(2)
    assert str(vector) == str([2])


def test_clear():
    vector = Vector()
    vector.add(1)
    vector.clear()
    assert str(vector) == str([])


def test_get():
    vector = Vector()
    vector.add(2)
    vector.add(6)
    vector.add(4)
    assert vector.get(1) == 6


def test_insert():
    vector = Vector()
    vector.add(1)
    vector.add(5)
    vector.insert(1, 3)
    assert vector.get(1) == 3


def test_is_empty():
    vector = Vector()
    assert vector.is_empty() is True
    vector.add(1)
    assert vector.is_empty() is False


def test_remove():
    vector = Vector()
    vector.add(1)
    vector.add(2)
    vector.add(3)
    assert vector.remove(1) == 2
    assert str(vector) == str([1, 3])


def test_set():
    vector = Vector()
    vector.add(1)
    vector.add(2)
    vector.add(3)
    vector.set(1, 7)
    assert vector.get(1) == 7


def test_size():
    vector = Vector()
    vector.add(1)
    assert vector.size() == 1


def test_to_string():
    vector = Vector()
    vector.add(1)
    assert vector.to_string() == str([1])


def test_count_in_range():
    vector = Vector()
    vector.add(28)
    vector.add(1)
    vector.add(17)
    vector.add(4)
    vector.add(41)
    vector.add(9)
    vector.add(59)
    vector.add(8)
    vector.add(31)
    vector.add(31)
    vector.add(30)
    vector.add(25)
    assert count_in_range(vector, 10, 30) == 4


def test_remove_all():
    vector = Vector()
    vector.add("a")
    vector.add("b")
    vector.add("c")
    vector.add("b")
    vector.add("b")
    vector.add("a")
    vector.add("b")
    remove_all(vector, "b")
    assert str(vector) == str(["a", "c", "a"])
