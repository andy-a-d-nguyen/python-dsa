import pytest

from queue.queue import Queue
from queue.queue import LinkedList
from queue.queue import Node
from queue.queue import stutter
from queue.queue import mirror


def test_add():
    ll = LinkedList()
    ll.add(1)
    assert ll.head.value == 1
    ll.add(2)
    assert ll.head.next.value == 2


def test_get():
    ll = LinkedList()
    with pytest.raises(IndexError) as message:
        ll.get(0)
    assert message.value.args[0] == 'List is empty'
    ll.add(1)
    assert ll.get(0) == 1
    ll.add(2)
    assert ll.get(1) == 2


def test_remove():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    assert ll.remove(0) == 1
    ll.add(3)
    ll.add(4)
    assert ll.remove(2) == 4


def test_queue():
    q = Queue()
    assert str(q) == str(LinkedList())


def test_enqueue():
    q = Queue()
    q.enqueue(Node(1))
    assert q.queue.head.value == 1


def test_dequeue():
    q = Queue()
    with pytest.raises(IndexError) as message:
        q.dequeue()
    assert message.value.args[0] == 'Queue is empty'
    q.enqueue(Node(1))
    assert q.dequeue() == 1


def test_is_empty():
    q = Queue()
    assert q.is_empty() is True


def test_peek():
    q = Queue()
    with pytest.raises(IndexError) as message:
        q.peek()
    assert message.value.args[0] == 'Queue is empty'
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    assert q.peek() == 1


def test_size():
    q = Queue()
    assert q.size() == 0
    q.enqueue(Node(1))
    assert q.size() == 1


def test_stutter():
    q = Queue()
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    q.enqueue(Node(3))
    result = stutter(q)
    assert result.size() == 6
    assert result.dequeue() == 1
    assert result.dequeue() == 1


def test_mirror():
    q = Queue()
    q.enqueue(Node(1))
    q.enqueue(Node(2))
    q.enqueue(Node(3))
    result = mirror(q)
    assert result.size() == 6
    assert result.dequeue() == 1
    assert result.dequeue() == 2
    assert result.dequeue() == 3
    assert result.dequeue() == 3
    assert result.dequeue() == 2
    assert result.dequeue() == 1
