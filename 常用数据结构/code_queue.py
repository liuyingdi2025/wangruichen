class Queue:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        self.values.append(value)
        return self

    def enqueue_batch(self, values):
        self.values.extend(values)
        return self

    def dequeue(self):
        value = self.values[0]
        self.values = self.values[1:]
        return value

    def front(self):
        return self.values[0]

    def traverse(self):
        print(' <- '.join([str(_) for _ in self.values]))