import pytest

from priority_queues_and_heaps.priority_queue_as_sorted_array import SortedArrayPQ


def test_enqueue():
    pq = SortedArrayPQ()
    pq.enqueue("a", 5)
    pq.enqueue("b", 1)
    assert pq.to_string() == str([{"value": "b", "priority": 1}, {"value": "a", "priority": 5}])
    with pytest.raises(ValueError) as error:
        pq.enqueue("b", 1)
    assert error.value.args[0] == "Value already exists in priority queue"


def test_dequeue():
    pq = SortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.dequeue()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 5)
    pq.enqueue("b", 1)
    assert pq.dequeue() == {"value": "b", "priority": 1}


def test_is_empty():
    pq = SortedArrayPQ()
    assert pq.is_empty() is True


def test_peek():
    pq = SortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.peek()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 5)
    pq.enqueue("b", 1)
    assert pq.peek() == {"value": "b", "priority": 1}


def test_peek_priority():
    pq = SortedArrayPQ()
    with pytest.raises(IndexError) as error:
        pq.peek_priority()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 5)
    pq.enqueue("b", 1)
    assert pq.peek_priority() == 1


def test_change_priority():
    pq = SortedArrayPQ()
    pq.enqueue("a", 5)
    pq.enqueue("b", 1)
    pq.change_priority("b", 2)
    assert pq.peek_priority() == 2
    pq.change_priority("b", 10)
    assert pq.peek_priority() == 5
