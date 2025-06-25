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
    def checkValidString(self, sequence: str) -> bool:
        p_stack = Stack()
        s_stack = Stack()
        for index in range(len(sequence)):
            seq = sequence[index]
            if seq == '(':
                p_stack.push(index)
            elif seq == '*':
                s_stack.push(index)
            else:  # seq == ')'
                if p_stack.not_empty():  # 优先匹配左括号
                    p_stack.pop()
                elif s_stack.not_empty():  # 如果左括号栈为空，则匹配星号栈
                    s_stack.pop()
                else:  # 如果左括号栈和星号栈均为空，则说明发现了不合群的右括号
                    return False
        # 此时考虑左括号栈是否为空，如果不为空，需要拿星号栈去匹配
        # 而且星号必须出现在左括号之后，例如 sequence = '**((' 不符合规则
        while p_stack.not_empty():
            if s_stack.is_empty():  # 存在不合群的左括号
                return False
            p_index = p_stack.pop()
            s_index = s_stack.pop()
            if s_index < p_index:
                return False
        # print(p_stack)
        # print(s_stack)
        return True


print(Solution().checkValidString('()'))  # True
print(Solution().checkValidString('(*)'))  # True
print(Solution().checkValidString('(*'))  # True
print(Solution().checkValidString('((*(*((*))'))  # True
print(Solution().checkValidString('*())'))  # True
print(Solution().checkValidString('*())'))  # True
print(Solution().checkValidString('(***'))  # True
print(Solution().checkValidString('**((()'))  # False: left parenthesis -> star
print(Solution().checkValidString('()))**'))  # False: star -> right parenthesis
print(Solution().checkValidString('()))'))  # False: star is not enough
print(Solution().checkValidString('((()'))  # False: star is not enough
print(Solution().checkValidString('(((*(*((*))'))  # False
