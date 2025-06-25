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
    def removeKdigits(self, sequence: str, k: int) -> str:
        if len(sequence) <= k:
            return '0'
        stack = Stack()
        counter = 0
        index = 0
        while index < len(sequence) and counter < k:
            number = ord(sequence[index]) - ord('0')
            if stack.is_empty() or stack.peek() <= number:
                stack.push(number)
            else:  # stack.peek() > number
                while stack.not_empty() and stack.peek() > number and counter < k:
                    # print(f'number={number}', stack, f'counter: {counter} -> {counter + 1}')
                    stack.pop()
                    counter += 1
                stack.push(number)
            index += 1
        while index < len(sequence):
            stack.push(ord(sequence[index]) - ord('0'))
            index += 1
        stack.values = stack.values[:len(sequence) - k]
        ans = stack.traverse_t2b(reverse=True)
        while ans.startswith('0'):
            ans = ans[1:]
        return ans if len(ans) > 0 else '0'


# sequence=2232113 k=3  2113
print(Solution().removeKdigits('33526221184202197273', 19))  # 123
