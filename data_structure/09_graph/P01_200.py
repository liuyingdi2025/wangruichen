from typing import *


class Solution:
    def __init__(self):
        self.ans = 0

    def solve(self, grid, row, column):
        if grid[row][column] == '1':
            grid[row][column] = '0'
            if row - 1 >= 0:
                self.solve(grid, row - 1, column)
            if row + 1 < len(grid):
                self.solve(grid, row + 1, column)
            if column - 1 >= 0:
                self.solve(grid, row, column - 1)
            if column + 1 < len(grid[0]):
                self.solve(grid, row, column + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.ans += 1
                    self.solve(grid, r, c)
        return self.ans


params = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands(grid=params))
