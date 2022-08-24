from typing import TypedDict, Union, List


class Item(TypedDict):
    value: Union[str, int]
    priority: int


class UnsortedArrayPQ:
    def __init__(self):
        self.priority_queue: List[Item] = []

    def enqueue(self, value: Union[str, int], priority):
        if len(self.priority_queue) > 0:
            for element in self.priority_queue:
                if element.get("value") == value:
                    raise ValueError("Value already exists in priority queue")
            self.priority_queue.append(Item(value=value, priority=priority))
        else:
            self.priority_queue.append(Item(value=value, priority=priority))

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            most_urgent = self.priority_queue[0]
            for i in range(1, len(self.priority_queue)):
                if self.priority_queue[i].get("priority") < most_urgent.get("priority"):
                    most_urgent = self.priority_queue[i]
                    self.priority_queue.pop(i)
            return most_urgent["value"]

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            most_urgent = self.priority_queue[0]
            for i in range(1, len(self.priority_queue)):
                if self.priority_queue[i].get("priority") < most_urgent.get("priority"):
                    most_urgent = self.priority_queue[i]
            return most_urgent

    def peek_priority(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        else:
            most_priority = self.priority_queue[0].get("priority")
            for i in range(1, len(self.priority_queue)):
                if self.priority_queue[i].get("priority") < most_priority:
                    most_priority = self.priority_queue[i].get("priority")
            return most_priority

    def is_empty(self):
        return len(self.priority_queue) == 0

    def size(self):
        return len(self.priority_queue)

    def change_priority(self, value, priority):
        for element in self.priority_queue:
            if element["value"] == value:
                element["priority"] = priority
                return  # If I don't return, function will continue and raise error
        raise ValueError("No such value in priority queue")

    def clear(self):
        self.priority_queue = []

    def to_string(self):
        return str(self.priority_queue)
