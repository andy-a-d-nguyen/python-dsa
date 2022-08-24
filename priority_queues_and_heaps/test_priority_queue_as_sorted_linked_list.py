import pytest

from priority_queues_and_heaps.priority_queue_as_sorted_linked_list import SortedLinkedListPQ


def test_enqueue():
    pq = SortedLinkedListPQ()
    pq.enqueue("b", 20)
    assert pq.to_string() == "{value: b, priority: 20}"
    with pytest.raises(ValueError) as error:
        pq.enqueue("b", 20)
    assert error.value.args[0] == "Value already exists in priority queue"
    pq.enqueue("a", 10)
    assert pq.to_string() == "{value: a, priority: 10} -> {value: b, priority: 20}"
    pq.enqueue("c", 15)
    with pytest.raises(ValueError) as error:
        pq.enqueue("b", 20)
    assert error.value.args[0] == "Value already exists in priority queue"
    assert pq.size() == 3
    assert pq.to_string() == "{value: a, priority: 10} -> {value: c, priority: 15} -> {value: b, priority: 20}"
    pq.enqueue("d", 15)
    assert pq.to_string() == "{value: a, priority: 10} -> {value: c, priority: 15} -> {value: d, priority: 15} -> {" \
                             "value: b, priority: 20}"


def test_dequeue():
    pq = SortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.dequeue()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    assert pq.dequeue() == "a"


def test_is_empty():
    pq = SortedLinkedListPQ()
    assert pq.is_empty() is True


def test_peek():
    pq = SortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.peek()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    assert str(pq.peek()) == "{value: a, priority: 10}"
    assert pq.size() == 3


def test_peek_priority():
    pq = SortedLinkedListPQ()
    with pytest.raises(IndexError) as error:
        pq.peek_priority()
    assert error.value.args[0] == "Priority queue is empty"
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    assert pq.peek_priority() == 10


def test_change_priority():
    pq = SortedLinkedListPQ()
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    pq.change_priority("b", 30)
    pq.dequeue()
    pq.dequeue()
    assert pq.peek_priority() == 30
    pq.enqueue("c", 15)
    assert pq.peek_priority() == 15
    pq.enqueue("a", 10)
    assert pq.peek_priority() == 10
    pq.change_priority("b", 5)
    assert pq.peek_priority() == 5


def test_clear():
    pq = SortedLinkedListPQ()
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    pq.clear()
    with pytest.raises(IndexError) as error:
        pq.peek()
    assert error.value.args[0] == "Priority queue is empty"
    assert pq.size() == 0
    assert pq.is_empty() is True
