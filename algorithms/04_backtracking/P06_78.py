from typing import *


class Solution:

    def __init__(self):
        self.numbers = []
        self.path = []
        self.paths = []

    def backtracking(self, count):
        self.paths.append([_ for _ in self.path])
        if count < len(self.numbers):
            for idx in range(count, len(self.numbers)):
                self.path.append(self.numbers[idx])
                self.backtracking(idx + 1)
                self.path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.numbers = nums
        self.backtracking(0)
        return self.paths


print(Solution().subsets([1, 2, 3]))
