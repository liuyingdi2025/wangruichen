from typing import *


class Solution:
    def __init__(self):
        self.numbers = []
        self.current = []
        self.myset = set()
        self.ans = []

    def backtracking(self):
        if len(self.current) == len(self.numbers):
            self.ans.append([_ for _ in self.current])
        else:
            for number in self.numbers:
                if number not in self.myset:
                    self.current.append(number)
                    self.myset.add(number)
                    self.backtracking()
                    self.current.pop()
                    self.myset.remove(number)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.numbers = nums
        self.backtracking()
        return self.ans


print(Solution().permute([1, 2, 3]))
