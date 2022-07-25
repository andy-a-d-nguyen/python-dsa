class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return str(self.head)


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, node):
        pass

    def __str__(self):
        return str(self.queue)
