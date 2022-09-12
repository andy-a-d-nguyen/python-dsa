# Priority Queue ADT

- Priority queue: Provides fast access to its highest-priority element
  - Enqueue: Adds an element at a given priority
  - Peek: Returns highest-priority value
  - Dequeue: Removes/returns the highest-priority value

## Priority Queue as Heap Array

- Heap: A special arrangement of elements in an array
  - The "start" or "root" index is 1 (index 0 is empty and unused)
  - Every index i has a "parent" index (i / 2) and two "child" indexes (i * 2, i * 2 + 1)
  - Ordering property: All parents have higher priorities (lower priority values) than their children
  - Enqueue: Place new element at first empty index
    - But now it may be out of order
    - So swap it upward with its parent until it is in order
  - Dequeue: Removing the highest priority element from a heap
    - First move the last element up to the start, index 1
    - Then swap it downward with its most-urgent child until in order
      - This process is called "bubbling down" or "percolating down"