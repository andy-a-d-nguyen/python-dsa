class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def add(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def clear(self):
        self.head = None

    def get(self, index):
        pass

    def insert(self, index, value):
        pass

    def is_empty(self):
        pass

    def remove(self, index):
        pass

    def set(self, index, value):
        pass

    def size(self):
        pass

    def to_string(self):
        return str(self.head)
