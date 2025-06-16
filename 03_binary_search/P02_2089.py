from typing import *


class Solution:
    def binary_search_left(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] < target:
            return self.binary_search_left(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return self.binary_search_left(nums, target, left, mid - 1)
        else:
            if mid == 0 or nums[mid - 1] < target:
                # 左侧小于 target
                return mid
            else:
                return self.binary_search_left(nums, target, left, mid - 1)

    def binary_search_right(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] < target:
            return self.binary_search_right(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return self.binary_search_right(nums, target, left, mid - 1)
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid
            else:
                return self.binary_search_right(nums, target, mid + 1, right)

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = self.binary_search_left(nums, target, 0, len(nums) - 1)
        if left == -1:
            return []
        right = self.binary_search_right(nums, target, 0, len(nums) - 1)
        return [_ for _ in range(left, right + 1)]
