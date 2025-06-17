from typing import *


class Solution:
    def product(self, nums, idx1, idx2, idx3):
        return nums[idx1] * nums[idx2] * nums[idx3]

    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 3:
            return self.product(nums, 0, 1, 2)
        if len(nums) == 4:
            return max([
                self.product(nums, 0, 1, 2),
                self.product(nums, 0, 1, 3),
                self.product(nums, 0, 2, 3),
                self.product(nums, 1, 2, 3)
            ])
        return max(
            self.product(nums, -1, -2, -3),
            self.product(nums, 0, 1, -1)
        )
