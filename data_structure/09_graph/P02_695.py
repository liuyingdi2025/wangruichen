from typing import *


class Solution:
    def __init__(self):
        self.max_area = 0

    def solve(self, grid, row, column, area=0):
        grid[row][column] = 0
        area += 1
        if row - 1 >= 0 and grid[row - 1][column] == 1:
            area = self.solve(grid, row - 1, column, area)
        if row + 1 < len(grid) and grid[row + 1][column] == 1:
            area = self.solve(grid, row + 1, column, area)
        if column - 1 >= 0 and grid[row][column - 1] == 1:
            area = self.solve(grid, row, column - 1, area)
        if column + 1 < len(grid[0]) and grid[row][column + 1] == 1:
            area = self.solve(grid, row, column + 1, area)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.solve(grid, r, c)
                    self.max_area = max(self.max_area, area)
        return self.max_area


params = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]
print(Solution().maxAreaOfIsland(grid=params))
