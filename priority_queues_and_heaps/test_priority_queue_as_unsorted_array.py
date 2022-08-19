import pytest

from priority_queues_and_heaps.priority_queue_as_unsorted_array import UnsortedArrayPQ, Item


def test_unsorted_array_pq():
    pq = UnsortedArrayPQ()
    assert pq.to_string() == str([])


def test_enqueue():
    pq = UnsortedArrayPQ()
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    assert pq.to_string() == str([{'value': 'John', 'priority': 5}, {'value': 100, 'priority': 2}])
    with pytest.raises(ValueError) as error:
        pq.enqueue("John", 5)
    assert error.value.args[0] == "Value already exists in priority queue"


def test_is_empty():
    pq = UnsortedArrayPQ()
    assert pq.is_empty() is True


def test_dequeue():
    pq = UnsortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.dequeue()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    assert pq.dequeue() == Item(value=100, priority=2)
    assert len(pq.priority_queue) == 1


def test_peek():
    pq = UnsortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.peek()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    assert pq.peek() == Item(value=100, priority=2)
    assert len(pq.priority_queue) == 2


def test_peek_priority():
    pq = UnsortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.peek_priority()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    assert pq.peek_priority() == 2


def test_size():
    pq = UnsortedArrayPQ()
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    assert pq.size() == 2


def test_change_priority():
    pq = UnsortedArrayPQ()
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    with pytest.raises(ValueError) as error:
        pq.change_priority(50, 50)
    assert error.value.args[0] == "No such value in priority queue"
    pq.change_priority(100, 1)
    assert pq.peek_priority() == 1


def test_clear():
    pq = UnsortedArrayPQ()
    pq.enqueue("John", 5)
    pq.enqueue(100, 2)
    pq.clear()
    assert pq.is_empty() is True
