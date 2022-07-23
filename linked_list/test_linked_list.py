import pytest

from linked_list.linked_list import LinkedList
from linked_list.linked_list import Node


def test_node():
    n = Node(1)
    assert n.value == 1


def test_linked_list():
    ll = LinkedList()
    assert ll.to_string() == "None"


def test_add():
    ll = LinkedList()
    n1 = Node(1)
    ll.add(n1)
    assert ll.head == n1
    n2 = Node(2)
    ll.add(n2)
    assert ll.head.next == n2
    assert ll.head.next.value == n2.value
    n3 = Node(3)
    ll.add(n3)
    assert n2.next == n3
    assert n2.next.value == n3.value


def test_clear():
    ll = LinkedList()
    n1 = Node(1)
    ll.add(n1)
    ll.clear()
    assert ll.to_string() == "None"


def test_get():
    ll = LinkedList()
    ll.add(Node(1))
    assert ll.get(0) == 1
    ll.add(Node(2))
    assert ll.get(1) == 2
    ll.add(Node(3))
    assert ll.get(2) == 3
    with pytest.raises(IndexError):
        ll.get(10)


def test_insert():
    ll = LinkedList()
    ll.insert(0, Node(1))  # [1]
    assert ll.get(0) == 1
    ll.add(Node(2))  # [1, 2]
    assert ll.get(0) == 1
    assert ll.get(1) == 2
    ll.insert(0, Node(4))  # [4, 1, 2]
    assert ll.get(0) == 4
    assert ll.get(1) == 1
    assert ll.get(2) == 2
    ll.insert(1, Node(3))  # [4, 3, 1, 2]
    assert ll.get(1) == 3
    with pytest.raises(IndexError):
        ll.insert(10, Node(10))


def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty() is True
    ll.add(Node(1))
    assert ll.is_empty() is False


def test_remove():
    ll = LinkedList()
    ll.add(Node(1))
    assert ll.remove(0) == 1
    with pytest.raises(IndexError):
        ll.remove(0)
    ll.add(Node(2))
    ll.add(Node(3))
    ll.add(Node(4))
    assert ll.remove(1) == 3


def test_set():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.set(1, Node(4))
    ll.set(0, Node(1))  # [1]
    assert ll.get(0) == 1
    ll.add(Node(2))  # [1, 2]
    assert ll.get(1) == 2
    ll.set(0, Node(5))  # [5, 2]
    assert ll.get(0) == 5
    assert ll.get(1) == 2
    ll.add(Node(3))  # [5, 2, 3]
    ll.set(1, Node(4))  # [5, 4, 3]
    assert ll.get(1) == 4
    with pytest.raises(IndexError):
        ll.set(10, Node(10))


def test_size():
    ll = LinkedList()
    assert ll.size() == 0
    ll.add(Node(1))
    assert ll.size() == 1
    ll.add(Node(2))
    assert ll.size() == 2
