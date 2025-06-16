from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = set()
        for num in nums:  # O(N)
            if num in numbers:
                numbers.remove(num)  # O(1)
            else:
                numbers.add(num)  # O(1)
        return list(numbers)[0]
