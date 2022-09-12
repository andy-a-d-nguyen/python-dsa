from __future__ import annotations

from typing import TypedDict, List


class Item(TypedDict):
    value: str | int
    priority: int


class HeapArrayPQ:
    def __init__(self):
        self.priority_queue: List[None | Item] = [None]

    def enqueue(self, value: str | int, priority: int):
        new_item = Item(value=value, priority=priority)
        self.priority_queue.append(new_item)
        current_index = len(self.priority_queue) - 1
        # loop until I get to the first item in the heap
        while current_index > 1:
            parent_index = current_index // 2
            # if my parent has a lower priority queue than me
            #   swap
            if self.priority_queue[parent_index]["priority"] > self.priority_queue[current_index]["priority"]:
                self.swap(parent_index, current_index)
            current_index = current_index // 2

    def dequeue(self):
        result = self.priority_queue.pop(1)
        temp = self.priority_queue.pop()
        self.priority_queue.insert(1, temp)
        current_index = 1
        while current_index < len(self.priority_queue):
            child_index1 = current_index * 2
            child_index2 = current_index * 2 + 1
            if child_index1 < len(self.priority_queue) and self.priority_queue[current_index]["priority"] > \
                    self.priority_queue[child_index1]["priority"]:
                self.swap(current_index, child_index1)
                current_index = child_index1
                continue
            elif child_index2 < len(self.priority_queue) and self.priority_queue[current_index]["priority"] > \
                    self.priority_queue[child_index2]["priority"]:
                self.swap(current_index, child_index2)
                current_index = child_index2
                continue
            else:
                current_index += 1
        return result

    def swap(self, index1, index2):
        temp = self.priority_queue[index1]
        self.priority_queue[index1] = self.priority_queue[index2]
        self.priority_queue[index2] = temp

    def to_string(self):
        return str(self.priority_queue)
