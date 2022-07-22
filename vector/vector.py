class Vector:
    def __init__(self):
        self.vector = []

    def add(self, value):
        self.vector.append(value)

    def clear(self):
        self.vector = []

    def get(self, index):
        return self.vector[index]

    def insert(self, index, value):
        self.vector.insert(index, value)

    def is_empty(self):
        return len(self.vector) == 0

    def remove(self, index):
        return self.vector.pop(index)

    def set(self, index, value):
        self.vector[index] = value

    def size(self):
        return len(self.vector)

    def to_string(self):
        return self.__str__()

    def __str__(self):
        return str(self.vector)


def count_in_range(vector: Vector, min: int, max: int):
    if vector.size() == 0:
        return 0
    count = 0
    for element in vector.vector:
        if min <= element <= max:
            count += 1
    return count


def remove_all(vector: Vector, character: str):
    if vector.size() == 0:
        return []
    # for index, element in reversed(list(enumerate(vector.vector))):
    #     if element == character:
    #         vector.remove(index)
    for index, element in enumerate(vector.vector):
        if element == character:
            vector.remove(index)
        # If the same character is repeated continuously,
        # after shifting the vector through the remove operation
        # a matching character will be moved into the spot that was checked
        if vector.get(index - 1) == character:
            vector.remove(index - 1)
