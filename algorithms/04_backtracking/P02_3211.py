from typing import *


class Solution:

    def __init__(self):
        self.length = -1
        self.items = ['0', '1']
        self.current = ''
        self.ans = []

    def backtracking(self):
        if len(self.current) == self.length:
            self.ans.append(self.current)
        else:
            for item in self.items:
                if item != '0' or len(self.current) == 0 or self.current[-1] != '0':
                    self.current += item
                    self.backtracking()
                    self.current = self.current[:-1]

    def validStrings(self, length: int) -> List[str]:
        if length == 1:
            return ['0', '1']
        self.length = length
        self.backtracking()
        return self.ans


print(Solution().validStrings(3))
