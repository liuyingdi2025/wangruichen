from typing import *


class Solution:
    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return self.binary_search(nums, target, left, mid - 1)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)
