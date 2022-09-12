from priority_queues_and_heaps.priority_queue_as_heap_array import HeapArrayPQ


def test_enqueue():
    pq = HeapArrayPQ()
    pq.enqueue("t", 2)
    pq.enqueue("m", 5)
    pq.enqueue("b", 4)
    pq.enqueue("x", 5)
    pq.enqueue("q", 5)
    pq.enqueue("a", 8)
    pq.enqueue("k", 1)
    assert pq.to_string() == str([
        None,
        {"value": "k", "priority": 1},
        {"value": "m", "priority": 5},
        {"value": "t", "priority": 2},
        {"value": "x", "priority": 5},
        {"value": "q", "priority": 5},
        {"value": "a", "priority": 8},
        {"value": "b", "priority": 4},
    ])


def test_dequeue():
    pq = HeapArrayPQ()
    pq.enqueue("k", 1)
    pq.enqueue("c", 2)
    pq.enqueue("f", 4)
    pq.enqueue("p", 7)
    pq.enqueue("e", 5)
    pq.enqueue("v", 8)
    pq.enqueue("y", 6)
    assert str(pq.dequeue()) == str({"value": "k", "priority": 1})
    assert pq.to_string() == str([
        None,
        {"value": "c", "priority": 2},
        {"value": "e", "priority": 5},
        {"value": "f", "priority": 4},
        {"value": "p", "priority": 7},
        {"value": "y", "priority": 6},
        {"value": "v", "priority": 8},
    ])
