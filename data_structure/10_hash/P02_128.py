from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mydict = dict()
        for num in nums:
            if num not in mydict:
                mydict[num] = 1

        max_length = 0
        for num in nums:
            if num in mydict:
                current = num + 1
                while current in mydict.keys():
                    mydict[num] += mydict[current]
                    mydict.pop(current)
                    current += 1
                max_length = max(max_length, mydict[num])
        return max_length


print(Solution().longestConsecutive(
    [100, 3, 200, 1, 4, 2]
))  # 4

print(Solution().longestConsecutive(
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
))  # 9

print(Solution().longestConsecutive(
    [1, 0, 1, 2]
))  # 3
