from typing import *


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

    def clear(self):
        self.values = []

    def __str__(self):
        return '|' + '|'.join([str(_) for _ in self.values]) + '|'


class Solution:
    def calc(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return int(num1 / num2)
        else:
            raise RuntimeError(f'invalid operator: {operator}')

    def evalRPN(self, tokens: List[str]) -> int:
        mystack = Stack()
        for token in tokens:
            # print(token, mystack)
            if token in ['+', '-', '*', '/']:
                num2 = mystack.pop()
                num1 = mystack.pop()
                mystack.push(self.calc(num1, num2, token))
            else:
                mystack.push(int(token))
        return mystack.pop()


print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
