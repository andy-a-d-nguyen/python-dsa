class Node:
    def __init__(self, value: object) -> object:
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
        if self.head is None:
            raise IndexError
        count = 0
        current_node = self.head
        # if we check the next node instead of the current node
        # when we get to the last node
        # because the last node's next node is None
        # while loop terminates
        # and last node is not checked
        while current_node is not None:
            if count == index:
                return current_node.value
            count += 1
            current_node = current_node.next
        raise IndexError

    def insert(self, index, node: Node):
        if self.head is None:
            if index == 0:
                self.head = node
            else:
                raise IndexError
        else:
            count = 0
            current_node = self.head
            next_node = self.head.next
            if index == 0:
                self.head = node
                node.next = current_node
                current_node.next = next_node
                return
            # We want to check if next node is None here
            # because we can't keep track of previous node
            # so this check is the same as assuming next node is current node
            # and current node is previous node
            while next_node is not None:
                count += 1
                if count == index:
                    current_node.next = node
                    node.next = next_node
                    break
                else:
                    current_node = current_node.next
                    next_node = next_node.next
            if count < index:
                raise IndexError

    def is_empty(self):
        return self.head is None

    def remove(self, index):
        if self.head is not None:
            if index == 0:
                current_node = self.head
                self.head = None
                return current_node.value
            elif index > 0:
                count = 0
                current_node = self.head
                next_node = self.head.next
                while next_node is not None:
                    count += 1
                    if count == index:
                        current_node.next = next_node.next
                        return next_node.value
                    else:
                        current_node = current_node.next
                        next_node = next_node.next
            else:
                raise IndexError
        else:
            raise IndexError

    def set(self, index, node: Node):
        if self.head is None:
            if index == 0:
                self.head = node
            else:
                raise IndexError
        else:
            current_node = self.head
            next_node = self.head.next
            if index == 0:
                self.head = node
                # if we assign current_node instead
                # the operation becomes an insert, not replace
                node.next = next_node
            elif index > 0:
                count = 0
                while next_node is not None:
                    count += 1
                    if count == index:
                        current_node.next = node
                        # if we point to next_node instead of next_node.next
                        # this operation becomes an insert, not replace
                        node.next = next_node.next
                        break
                    current_node = current_node.next
                    next_node = next_node.next
                if count < index:
                    raise IndexError
            else:
                raise IndexError

    def size(self):
        if self.head is None:
            return 0
        else:
            count = 1
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
                count += 1
            return count

    def to_string(self):
        return str(self.head)
