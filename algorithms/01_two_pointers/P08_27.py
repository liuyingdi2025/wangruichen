from typing import *


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        while left < len(nums) and nums[left] != val:
            left += 1
        right = left + 1
        while right < len(nums):
            while right < len(nums) and nums[right] == val:
                right += 1
            if right < len(nums):
                nums[left] = nums[right]
                left += 1
                right += 1
        return left


print(Solution().removeElement(
    nums=[3, 2, 2, 3], val=3
))
