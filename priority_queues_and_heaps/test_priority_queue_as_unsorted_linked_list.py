import pytest

from priority_queues_and_heaps.priority_queue_as_unsorted_linked_list import UnsortedLinkedListPQ, Node


def test_enqueue():
    pq = UnsortedLinkedListPQ()
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    assert pq.to_string() == "{value: a, priority: 20} -> {value: b, priority: 10}"
    with pytest.raises(ValueError) as error:
        pq.enqueue("a", 20)
    assert error.value.args[0] == "Value already exists in priority queue"
    pq.enqueue("c", 10)
    assert pq.to_string() == "{value: a, priority: 20} -> {value: b, priority: 10} -> {value: c, priority: 10}"


def test_dequeue():
    pq = UnsortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.dequeue()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    assert pq.dequeue() == "b"


def test_peek():
    pq = UnsortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.peek()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    assert str(pq.peek()) == str(Node("b", 10))


def test_peek_priority():
    pq = UnsortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.peek_priority()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    assert pq.peek_priority() == 10


def test_change_priority():
    pq = UnsortedLinkedListPQ()
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    pq.change_priority("b", 5)
    assert pq.peek_priority() == 5
    pq.change_priority("b", 30)
    assert pq.peek_priority() == 20


def test_clear():
    pq = UnsortedLinkedListPQ()
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    pq.clear()
    assert pq.is_empty() is True


def test_size():
    pq = UnsortedLinkedListPQ()
    pq.enqueue("a", 20)
    pq.enqueue("b", 10)
    assert pq.size() == 2
    pq.dequeue()
    assert pq.size() == 1
