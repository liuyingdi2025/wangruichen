from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1, idx2, pointer = m - 1, n - 1, m + n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[pointer] = nums1[idx1]
                idx1 -= 1
                pointer -= 1
            else:
                nums1[pointer] = nums2[idx2]
                idx2 -= 1
                pointer -= 1
        while idx2 >= 0:
            nums1[pointer] = nums2[idx2]
            idx2 -= 1
            pointer -= 1


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
Solution().merge(nums1, 3, nums2, 3)
print(nums1)
