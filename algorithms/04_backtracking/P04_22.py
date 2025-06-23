from typing import *


class Solution:

    def __init__(self):
        self.length = 0
        self.items = {'(': -1, ')': 1}
        self.current = ''
        self.counter = 0
        self.ans = []

    def backtracking(self):
        if len(self.current) == self.length:
            if self.counter == 0:
                self.ans.append(self.current)
        else:
            for item in self.items.keys():
                if self.counter + self.items[item] <= 0:
                    self.current += item
                    self.counter += self.items[item]
                    self.backtracking()
                    self.current = self.current[:-1]
                    self.counter -= self.items[item]

    def generateParenthesis(self, count: int) -> List[str]:
        self.length = 2 * count
        self.backtracking()
        return self.ans


print(Solution().generateParenthesis(3))
