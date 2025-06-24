from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                right += 1
            if right < len(nums):
                nums[left + 1] = nums[right]
                left += 1
        return left + 1


print(Solution().removeDuplicates(
    nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
))
