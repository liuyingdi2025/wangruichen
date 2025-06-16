from typing import *


class Solution:

    def search_left(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] < target:  # 必须向右寻找
            return self.search_left(nums, target, mid + 1, right)
        elif nums[mid] > target:  # 必须向左寻找
            return self.search_left(nums, target, left, mid - 1)
        else:  # nums[mid] == target
            if mid == 0 or nums[mid - 1] < target:  # 左侧不存在 或 左侧小于target
                return mid
            else:  # 左侧存在 并且 左侧等于target，必须向左寻找
                return self.search_left(nums, target, left, mid - 1)

    def search_right(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if nums[mid] < target:  # 必须向右寻找
            return self.search_right(nums, target, mid + 1, right)
        elif nums[mid] > target:  # 必须向左寻找
            return self.search_right(nums, target, left, mid - 1)
        else:  # nums[mid] == target
            if mid == len(nums) - 1 or nums[mid + 1] > target:  # 右侧不存在 或 右侧大于target
                return mid
            else:  # 右侧存在 并且 右侧等于target，必须向右寻找
                return self.search_right(nums, target, mid + 1, right)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_left(nums, target, 0, len(nums) - 1)
        if left == -1:
            return [-1, -1]
        right = self.search_right(nums, target, 0, len(nums) - 1)
        return [left, right]


print(Solution().searchRange([1, 2, 2, 3], 2))
print(Solution().searchRange([2, 2], 2))
