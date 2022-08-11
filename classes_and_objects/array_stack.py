class ArrayStack:
    def __init__(self):
        self.elements = [None] * 10
        self.size = 0
        self.capacity = 10

    def push(self, n: int):
        # For fixed size array
        # if self.size == self.capacity:
        #     raise IndexError("Capacity exceeded")
        if self.size == self.capacity - 1:
            self.elements += [None] * self.capacity
            self.capacity *= 2
        self.elements[self.size] = n
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('List is empty')
        popped_element = self.elements[self.size - 1]
        self.elements[self.size - 1] = None
        self.size -= 1
        if self.size < self.capacity / 2:
            self.elements = self.elements[:(self.capacity // 2)]
            self.capacity //= 2
        return popped_element

    def peek(self):
        if self.size == 0:
            raise IndexError('List is empty')
        return self.elements[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def to_string(self):
        return str(self.elements[:self.size])