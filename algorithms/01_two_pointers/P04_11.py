from typing import *


class Solution:
    def calc_area(self, heights, left, right):
        return (right - left) * min(heights[left], heights[right])

    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        L, R, max_area = left, right, self.calc_area(heights, left, right)
        while left < right:
            if heights[left] < heights[right]:
                # left 向右，期望找一个更大的 left height
                left += 1
                while left < right and heights[left] <= heights[L]:
                    left += 1
            elif heights[left] > heights[right]:
                # right 向左，期望找一个更大的 right height
                right -= 1
                while left < right and heights[right] <= heights[R]:
                    right -= 1
            else:  # heights[left] == heights[right]
                # left 向右，期望找一个更大的 left height
                left += 1
                while left < right and heights[left] <= heights[L]:
                    left += 1
                # right 向左，期望找一个更大的 right height
                right -= 1
                while left < right and heights[right] <= heights[R]:
                    right -= 1
            if left < right:
                area = self.calc_area(heights, left, right)
                if area >= max_area:
                    L, R, max_area = left, right, area
        return max_area


print(Solution().maxArea(
    heights=[
        76, 155, 15, 188, 180, 154, 84, 34, 187, 142,
        22, 5, 27, 183, 111, 128, 50, 58, 2, 112,
        179, 2, 100, 111, 115, 76, 134, 120, 118, 103,
        31, 146, 58, 999, 134, 38, 104, 170, 25, 92,
        112, 199, 49, 140, 135, 160, 20, 185, 171, 23,
        98, 150, 177, 98, 61, 92, 26, 147, 164, 144,
        51, 196, 42, 109, 194, 177, 100, 99, 99, 125,
        143, 12, 76, 192, 152, 11, 152, 124, 197, 123,
        147, 95, 73, 124, 45, 86, 168, 24, 34,
        133, 120, 85, 81, 163, 146, 75, 92, 199, 126, 191
    ]
))
