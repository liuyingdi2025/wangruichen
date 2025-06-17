from typing import *


class Solution:
    def binary_search(self, nums, target, left, right):
        mid = (left + right) // 2
        if nums[mid] < target:  # nums[mid] = 8 < target = 10
            # 目标可能在 mid 的右侧，也可能目标不存在
            if mid == right or nums[mid + 1] > target:
                # 右侧没有元素 或者 右侧元素大于 target
                return mid + 1
            else:
                # 右侧有元素 并且 右侧元素小于等于 target
                return self.binary_search(nums, target, mid + 1, right)
        elif nums[mid] > target:  # target = 10 < nums[mid] = 12
            # 目标可能在 mid 的左侧，也可能目标不存在
            if mid == left or nums[mid - 1] < target:
                # 左侧没有元素 或者 左侧元素小于 target
                return mid
            else:
                # 左侧有元素 并且 左侧元素大于等于 target
                return self.binary_search(nums, target, left, mid - 1)
        else:  # nums[mid] == target
            return mid

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)


print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 7))
