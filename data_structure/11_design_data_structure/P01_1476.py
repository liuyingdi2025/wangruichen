from typing import *


class SubrectangleQueries:

    def __init__(self, values: List[List[int]]):
        self.values = values

    def updateSubrectangle(self, r1: int, c1: int, r2: int, c2: int, value: int) -> None:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                self.values[r][c] = value

    def getValue(self, r: int, c: int) -> int:
        return self.values[r][c]
