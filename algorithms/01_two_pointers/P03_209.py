from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_length = len(nums)
        left, right = 0, 0  # [left, right]
        current_sum = nums[0]
        while left < len(nums):
            # print(nums[left:right + 1])
            if current_sum < target:
                if right + 1 < len(nums):
                    right += 1
                    current_sum += nums[right]
                else:
                    break
            else:  # curr_sum >= target
                # print(nums[left:right + 1], current_sum)
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length


print(Solution().minSubArrayLen(
    target=7,
    nums=[2, 3, 1, 2, 4, 3]
))  # 13
