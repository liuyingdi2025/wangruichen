from typing import *


class Solution:
    def calc_min_days(self, weights, capability):
        days = 0
        index = 0
        current_weight = 0
        while index < len(weights):
            if current_weight + weights[index] <= capability:
                current_weight += weights[index]
                index += 1
            else:
                days += 1
                current_weight = 0
        if current_weight > 0:
            days += 1
        return days

    def binary_search(self, weights, target, left, right):
        if left >= right:
            return left
        mid = (left + right) // 2
        if self.calc_min_days(weights, mid) <= target:
            return self.binary_search(weights, target, left, mid)
        else:  # weights[mid] > target:
            return self.binary_search(weights, target, mid + 1, right)

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_value = max(weights)
        max_value = sum(weights)
        return self.binary_search(weights, days, min_value, max_value)


print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 15
print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3))  # 6
print(Solution().shipWithinDays([1, 2, 3, 1, 1], 4))  # 3
