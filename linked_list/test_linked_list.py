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
    n3 = Node(3)
    ll.add(n3)
    assert n2.next == n3


def test_clear():
    ll = LinkedList()
    n1 = Node(1)
    ll.add(n1)
    ll.clear()
    assert ll.to_string() == "None"
