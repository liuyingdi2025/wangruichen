from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for idx in range(len(nums)):
            if target - nums[idx] in mydict:
                return [mydict[target - nums[idx]], idx]
            mydict[nums[idx]] = idx
        return [-1, -1]
