class Stack:
    def __init__(self):
        self.values = []

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

    def get(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        return self.values[-1]


class Solution:
    def isValid(self, text: str) -> bool:
        mapper = {
            '(': -1, ')': 1,
            '[': -2, ']': 2,
            '{': -3, '}': 3
        }
        stack = Stack()
        for char in text:
            if mapper[char] < 0:
                # mapper[char] < 0
                stack.push(mapper[char])
            elif stack.is_empty():
                # stack is empty
                return False
            elif mapper[char] + stack.get() != 0:
                # not match
                return False
            else:
                stack.pop()
        return stack.is_empty()
