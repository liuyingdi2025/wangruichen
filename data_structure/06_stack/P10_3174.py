from typing import *


class Stack:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return len(self.values) == 0

    def not_empty(self):
        return len(self.values) > 0

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        item = self.values[-1]
        self.values = self.values[:-1]
        return item

    def peek(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        return self.values[-1]

    def traverse_t2b(self, reverse=False):
        values = self.values if reverse else self.values[::-1]
        return ''.join([str(_) for _ in values])

    def clear(self):
        self.values = []

    def __str__(self):
        return '|' + '|'.join([str(_) for _ in self.values]) + '|'


class Solution:
    def clearDigits(self, sequence: str) -> str:
        stack = Stack()
        for ch in sequence:
            if ch.isdigit():
                if stack.not_empty():
                    stack.pop()
            else:
                stack.push(ch)
        return stack.traverse_t2b(reverse=True)

print(Solution().clearDigits(sequence='abc'))
print(Solution().clearDigits(sequence='abcd34'))