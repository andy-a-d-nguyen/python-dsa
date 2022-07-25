from queue.queue import Queue
from queue.queue import LinkedList
from queue.queue import Node


def test_queue():
    q = Queue()
    assert str(q) == str(LinkedList())


def test_enqueue():
    q = Queue()
    assert False
