class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0 if self.head is None else 1

    def add(self, value):
        n = Node(value)
        if self.head is None:
            self.head = n
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = n
        self.length += 1

    def get(self, index):
        if self.head is None:
            raise IndexError('List is empty')
        else:
            count = 0
            current_node = self.head
            while current_node is not None:
                if count == index:
                    return current_node.value
                else:
                    count += 1
                    current_node = current_node.next

    def remove(self, index):
        if self.head is None:
            raise IndexError('List is empty')
        else:
            count = 0
            current_node = self.head
            next_node = self.head.next
            if index == 0:
                self.length -= 1
                self.head = next_node
                return current_node.value
            else:
                while next_node is not None:
                    count += 1
                    if count == index:
                        current_node.next = next_node.next
                        self.length -= 1
                        return next_node.value
                    else:
                        current_node = current_node.next
                        next_node = next_node.next
                if index > count:
                    raise IndexError('Index out of range')

    def is_empty(self):
        return self.head is None

    def __str__(self):
        return str(self.head)


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def dequeue(self):
        if self.queue.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.queue.remove(0)

    def enqueue(self, node):
        self.queue.add(node.value)

    def is_empty(self):
        return self.queue.is_empty()

    def peek(self):
        if self.queue.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.queue.get(0)

    def size(self):
        return self.queue.length

    def __str__(self):
        return str(self.queue)


def stutter(queue):
    result = Queue()

    while queue.size() > 0:
        current_value = queue.dequeue()
        result.enqueue(Node(current_value))
        result.enqueue(Node(current_value))

    return result


def mirror(queue):
    values = []
    size = queue.size()
    for _ in range(size):
        current_value = queue.dequeue()
        queue.enqueue(Node(current_value))
        values.append(current_value)
    for value in reversed(values):
        queue.enqueue(Node(value))
    return queue
