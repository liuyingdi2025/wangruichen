from typing import *


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = list()
        for idx in range(0, len(nums) - 1, 2):
            ans.append(nums[idx + 1])
            ans.append(nums[idx])
        return ans
