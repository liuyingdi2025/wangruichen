from typing import *


class Solution:
    def calc_flowers(self, periods, neighbors, day):
        result = 0
        counter = 0
        index = 0
        while index < len(periods):
            print(periods, index, counter, result)
            if periods[index] <= day:
                counter += 1
                if counter == neighbors:
                    result += 1
                    counter = 0
            index += 1
        return result

    def binary_search(self, periods, target, left, right, neighbors):
        print(periods, left, right)
        if left == right:
            return left
        mid = (left + right) // 2
        if self.calc_flowers(periods, neighbors, mid) < target:
            # 未完成任务，必须向右探索
            return self.binary_search(periods, target, mid + 1, right, neighbors)
        else:
            # 完成任务：尝试向左侧探索
            return self.binary_search(periods, target, left, mid, neighbors)

    def minDays(self, periods: List[int], flowers: int, neighbors: int) -> int:
        if len(periods) < flowers * neighbors:
            return -1
        min_value = min(periods)
        max_value = max(periods)
        return self.binary_search(periods, flowers, min_value, max_value, neighbors)


# print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))  # 3
# print(Solution().minDays([1, 10, 3, 10, 2], 3, 2))  # -1
# print(Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))  # 12
# print(Solution().minDays([1000000000, 1000000000], 1, 1))  # 1000000000
# print(Solution().minDays([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2))  # 9

print(Solution().calc_flowers(periods=[1, 10, 3, 10, 2], neighbors=1, day=3))