from typing import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        while left < len(nums) and nums[left] != nums[left - 2]:
            left += 1
        right = left + 1
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left - 2]:
                right += 1
            if right < len(nums):
                nums[left] = nums[right]
                left += 1
                right += 1
        # print(nums)
        return left


# nums[right]  vs. nums[left - 2]
# 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3
#             L  R
# 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3
#             L     R
# 0, 0, 1, 1, 2, 1, 2, 2, 2, 2, 2, 3, 3, 3
#                L     R
# 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3
#                   L     R
# 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3
#                   L              R
# 0, 0, 1, 1, 2, 2, 3, 2, 2, 2, 2, 3, 3, 3
#                      L              R
# 0, 0, 1, 1, 2, 2, 3, 3, 2, 2, 2, 3, 3, 3
#                         L              R
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]))
