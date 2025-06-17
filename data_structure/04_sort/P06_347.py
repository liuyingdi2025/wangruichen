from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
        nums = list(counter.keys())
        # print(counter, nums)
        for idx in range(k):
            max_idx = idx
            for t in range(idx + 1, len(nums)):
                if counter[nums[t]] > counter[nums[max_idx]]:
                    max_idx = t
            nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
        return nums[:k]


print(Solution().topKFrequent([1, 2], 2))
