from typing import *


class Node:
    def __init__(self, value, greater=None):
        self.value = value
        self.greater = greater


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
    def nextGreaterElements(self, numbers: List[int]) -> List[int]:
        numbers.extend(numbers)
        nodes = [Node(_) for _ in numbers]
        stack = Stack()
        for node in nodes:
            if stack.is_empty() or stack.peek().value >= node.value:
                stack.push(node)
                continue
            # stack.is not empty and stack.peek() < node.value
            while stack.not_empty() and stack.peek().value < node.value:
                stack.pop().greater = node.value
            stack.push(node)
        while stack.not_empty():
            stack.pop().greater = -1
        return [nodes[_].greater for _ in range(len(numbers) // 2)]


print(Solution().nextGreaterElements([4, 1, 2, 3, 4, 3]))  # [-1, 2, 3, 4, -1, 4]
