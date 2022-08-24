from __future__ import annotations

from typing import TypedDict, List


class Item(TypedDict):
    value: str | int
    priority: int


class SortedArrayPQ:
    def __init__(self):
        self.priority_queue: List[Item] = []

    def enqueue(self, value: str | int, priority: int):
        if self.is_empty():
            self.priority_queue.append(Item(value=value, priority=priority))
        else:
            for index in range(len(self.priority_queue)):
                if value == self.priority_queue[index]["value"]:
                    raise ValueError("Value already exists in priority queue")
                if priority < self.priority_queue[index]["priority"]:
                    self.priority_queue.insert(index, Item(value=value, priority=priority))

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.priority_queue.pop(0)["value"]

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.priority_queue[0]

    def peek_priority(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            return self.priority_queue[0]["priority"]

    def change_priority(self, value: str | int, priority: int):
        for item in self.priority_queue:
            if item["value"] == value:
                item["priority"] = priority
        for i in range(len(self.priority_queue)):
            swapped = False
            # - i because we don't need to check elements we have passed through in the outer loop
            # - 1 because we don't want to get to the last element and then check the element after it causing out of
            # index error
            for j in range(len(self.priority_queue) - i - 1):
                if self.priority_queue[j]["priority"] > self.priority_queue[j + 1]["priority"]:
                    self.priority_queue[j], self.priority_queue[j + 1] = self.priority_queue[j + 1], \
                                                                         self.priority_queue[j]
                    swapped = True
            # If no swap happened in the inner loop, queue is already sorted so stop looping
            if swapped is False:
                break

    def clear(self):
        self.priority_queue = []

    def is_empty(self):
        return len(self.priority_queue) == 0

    def size(self):
        return len(self.priority_queue)

    def to_string(self):
        return str(self.priority_queue)
