class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            raise Exception('List is empty')
        else:
            return self.stack[-1]

    def pop(self):
        if self.is_empty():
            raise Exception('List is empty')
        else:
            return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


def check_balance(source):
    s = Stack()
    for i in range(len(source)):
        if source[i] == '{' or source[i] == '(':
            s.push(source[i])
        elif source[i] == '}':
            if not s.is_empty() and s.peek() == '{':
                s.pop()
            else:
                return i
        elif source[i] == ')':
            if not s.is_empty() and s.peek() == '(':
                s.pop()
            else:
                return i
    if s.is_empty():
        return -1
    else:
        return len(source)
