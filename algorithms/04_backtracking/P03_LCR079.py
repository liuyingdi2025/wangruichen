from typing import *


class Solution:

    def __init__(self):
        self.items = []
        self.current = []
        self.ans = []

    def backtracking(self):
        self.ans.append([_ for _ in self.current])
        if len(self.current) < len(self.items):
            for item in self.items:
                if len(self.current) == 0 or item > self.current[-1]:
                    self.current.append(item)
                    self.backtracking()
                    self.current.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.items = nums
        self.backtracking()
        return self.ans


print(Solution().subsets([5, 0]))
