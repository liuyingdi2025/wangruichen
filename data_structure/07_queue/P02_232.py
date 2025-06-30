from typing import *


class Stack:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.values.append(value)
        return self

    def peek(self):
        return self.values[-1]

    def pop(self):
        value = self.values[-1]
        self.values = self.values[:-1]
        return value


class MyQueue:

    def __init__(self):
        self.stack = Stack()
        self.stack_tmp = Stack()

    def empty(self) -> bool:
        return self.stack.is_empty()

    def push(self, value: int) -> None:
        while not self.stack.is_empty():
            self.stack_tmp.push(self.stack.pop())
        self.stack.push(value)
        while not self.stack_tmp.is_empty():
            self.stack.push(self.stack_tmp.pop())

    def peek(self) -> int:
        return self.stack.peek()

    def pop(self) -> int:
        return self.stack.pop()
