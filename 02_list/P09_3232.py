from typing import *


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a, b = 0, 0
        for num in nums:
            if num < 10:
                a += num
            else:
                b += num
        return a != b
