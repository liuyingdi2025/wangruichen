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
    def decodeString(self, text: str) -> str:
        mystack = Stack()
        digit = ''
        for ch in text:
            if ch.isalpha() or ch == '[':
                if len(digit) > 0:
                    mystack.push(digit)
                    digit = ''
                mystack.push(ch)
            elif ch.isdigit():
                digit += ch
            else:
                string = ''
                while True:
                    current = mystack.pop()
                    if current == '[':
                        mystack.push(int(mystack.pop()) * string)
                        break
                    string = current + string
        return mystack.traverse_t2b(reverse=True)


print(Solution().decodeString('100[leetcode]'))
