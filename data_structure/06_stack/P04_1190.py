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

    def clear(self):
        ans = ''
        while self.not_empty():
            ans += self.pop()
        return ans

    def __str__(self):
        return '|' + '|'.join([str(_) for _ in self.values]) + '|'


class Solution:
    def reverseParentheses(self, text: str) -> str:
        mystack = Stack()
        for ch in text:
            if ch != ')':
                mystack.push(ch)
                continue
            string = ''
            while True:
                current = mystack.pop()
                if current == '(':
                    break
                string = current + string
            mystack.push(string[::-1])
        ans = ''
        while mystack.not_empty():
            ans = mystack.pop() + ans
        return ans


print(Solution().reverseParentheses('a(bcdefghijkl(mno)p)q'))
