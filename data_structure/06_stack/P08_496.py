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
    def nextGreaterElement(self, targets: List[int], numbers: List[int]) -> List[int]:
        mydict = dict()
        stack = Stack()
        for number in numbers:
            if stack.is_empty() or number < stack.peek():
                stack.push(number)
                continue
            # stack is not empty and number > stack.peek()
            while stack.not_empty() and stack.peek() < number:
                mydict[stack.pop()] = number
            stack.push(number)
        while stack.not_empty():
            mydict[stack.pop()] = -1
        return [mydict[_] for _ in targets]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 2, 4]))  # [-1, 3, 4]
