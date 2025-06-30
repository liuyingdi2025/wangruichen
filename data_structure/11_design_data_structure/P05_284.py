from typing import *


class PeekingIterator:
    def __init__(self, iterator):
        self.values = []
        while iterator.hasNext():
            self.values.append(iterator.next())
        self.pointer = 0

    def peek(self):
        return self.values[self.pointer]

    def next(self):
        self.pointer += 1
        return self.values[self.pointer - 1]

    def hasNext(self):
        return self.pointer < len(self.values)
