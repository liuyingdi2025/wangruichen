from typing import *


class Solution:

    def __init__(self):
        self.sequence = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.digits = []  # ['abc', 'def']
        self.combination = ''
        self.ans = []

    def backtracking(self, index=0):
        if index == len(self.digits):
            self.ans.append(self.combination)
        else:
            for character in self.digits[index]:
                self.combination += character
                self.backtracking(index + 1)
                self.combination = self.combination[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.digits = [self.sequence[int(_)] for _ in digits]
        self.backtracking()
        return self.ans


print(Solution().letterCombinations('23'))
