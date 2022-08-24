from __future__ import annotations


class Node:
    def __init__(self, value: str | int, priority: int, next: Node = None):
        self.value = value
        self.priority = priority
        self.next = next

    def __str__(self):
        return f"{{value: {self.value}, priority: {self.priority}}}"


class SortedLinkedListPQ:
    def __init__(self, head: Node = None):
        self.head = head
        self.count = 0

    def enqueue(self, value: str | int, priority: int):
        if self.head is None:
            self.head = Node(value, priority)
            self.count += 1
        else:
            new_node = Node(value, priority)
            if value == self.head.value:
                raise ValueError("Value already exists in priority queue")
            else:
                # Special handling of head because I can't set new node to be head if I check for current instead of
                # current.next in a while loop and I have to check for current.next because otherwise, I lose access to
                # the preceding node if I were to check for current
                if priority < self.head.priority:
                    new_node.next = self.head
                    self.head = new_node
                    self.count += 1
                    return
                else:
                    current = self.head
                    while current.next is not None:
                        if value == current.next.value:
                            raise ValueError("Value already exists in priority queue")
                        else:
                            if priority < current.next.priority:
                                next_node = current.next
                                current.next = new_node
                                new_node.next = next_node
                                break
                            else:
                                current = current.next
                    self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            most_urgent = self.head
            self.head = self.head.next
            self.count -= 1
            return most_urgent.value

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.head

    def peek_priority(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.head.priority

    def change_priority(self, value: str | int, priority: int):
        if self.head.next is None:
            if self.head.value == value:
                self.head.priority = priority
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next.priority = priority
                    if current.priority > current.next.priority:
                        misplaced_node = current.next
                        current.next = current.next.next
                        self.count -= 1
                        self.enqueue(misplaced_node.value, misplaced_node.priority)
                    break
                else:
                    current = current.next

    def clear(self):
        self.head = None
        self.count = 0
        pass

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current)
            if current.next is not None:
                result += " -> "
            current = current.next
        return result


if __name__ == '__main__':
    pq = SortedLinkedListPQ()
    pq.enqueue("b", 20)
    pq.enqueue("a", 10)
    pq.enqueue("c", 15)
    print(pq.to_string())
    pq.change_priority("b", 30)
    print(pq.to_string())
    pq.dequeue()
    pq.dequeue()
    print(pq.to_string())
    pq.enqueue("c", 15)
    print(pq.to_string())
    pq.enqueue("a", 10)
    print(pq.to_string())
