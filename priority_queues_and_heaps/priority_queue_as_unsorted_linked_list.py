from __future__ import annotations


class Node:
    def __init__(self, value: str | int, priority: int, next: Node = None):
        self.value = value
        self.priority = priority
        self.next = next

    def __str__(self):
        return f"{{value: {self.value}, priority: {self.priority}}}"


class UnsortedLinkedListPQ:
    def __init__(self, head: Node = None):
        self.head = head
        self.count = 0

    def enqueue(self, value: str | int, priority: int):
        if self.head is None:
            self.head = Node(value, priority)
        else:
            current = self.head
            while current.next is not None:
                if current.value == value:
                    raise ValueError("Value already exists in priority queue")
                else:
                    current = current.next
            current.next = Node(value, priority)
        self.count += 1

    def dequeue(self):
        if self.head is None:
            raise IndexError("Priority queue is empty")
        else:
            current = self.head
            most_urgent = self.head
            while current.next is not None:
                if current.next.priority < most_urgent.priority:
                    most_urgent = current.next
                    current.next = current.next.next
            self.count -= 1
            return most_urgent.value

    def peek(self):
        if self.head is None:
            raise IndexError("Priority queue is empty")
        else:
            current = self.head
            most_urgent = self.head
            while current is not None:
                if current.priority < most_urgent.priority:
                    most_urgent = current
                else:
                    current = current.next
            return most_urgent

    def peek_priority(self):
        if self.head is None:
            raise IndexError("Priority queue is empty")
        else:
            current = self.head
            most_urgent = self.head
            while current is not None:
                if current.priority < most_urgent.priority:
                    most_urgent = current
                else:
                    current = current.next
            return most_urgent.priority

    def change_priority(self, value: str | int, priority: int):
        current = self.head
        while current is not None:
            if current.value == value:
                current.priority = priority
                # Not sure why not breaking or returning causes an infinite loop
                # But breaking or returning is not necessary if there is no else block
                break
            else:
                current = current.next

    def clear(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

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
