from typing import *


class NeighborSum:

    def __init__(self, values: List[List[int]]):
        self.values = values
        self.mapper = dict()
        for r in range(len(values)):
            for c in range(len(values[0])):
                self.mapper[self.values[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.mapper[value]
        ans = 0
        if r - 1 >= 0:
            ans += self.values[r - 1][c]
        if r + 1 < len(self.values):
            ans += self.values[r + 1][c]
        if c - 1 >= 0:
            ans += self.values[r][c - 1]
        if c + 1 < len(self.values[0]):
            ans += self.values[r][c + 1]
        return ans

    def diagonalSum(self, value: int) -> int:
        r, c = self.mapper[value]
        ans = 0
        if r - 1 >= 0 and c - 1 >= 0:
            ans += self.values[r - 1][c - 1]
        if r - 1 >= 0 and c + 1 < len(self.values[0]):
            ans += self.values[r - 1][c + 1]
        if r + 1 < len(self.values) and c - 1 >= 0:
            ans += self.values[r + 1][c - 1]
        if r + 1 < len(self.values) and c + 1 < len(self.values[0]):
            ans += self.values[r + 1][c + 1]
        return ans
