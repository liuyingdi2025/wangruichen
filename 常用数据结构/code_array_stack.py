class Stack:
    def __init__(self):
        # Bottom | Head -> ... -> ... -> None | Top
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def not_empty(self):
        return not self.is_empty()

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        item = self.values[-1]
        self.values = self.values[:-1]
        return item

    def get(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        return self.values[-1]
