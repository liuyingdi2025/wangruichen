from typing import *


class Solution:
    def calculate_days(self, piles, speed):
        time = 0
        for pile in piles:
            if pile % speed == 0:
                time += (pile // speed)
            else:
                time += pile // speed + 1
        return time

    def binary_search(self, piles, target, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if self.calculate_days(piles, mid) <= target:
            return self.binary_search(piles, target, left, mid)
        else:
            return self.binary_search(piles, target, mid + 1, right)

    def minEatingSpeed(self, piles: List[int], target: int) -> int:
        return self.binary_search(piles, target, 1, max(piles))
