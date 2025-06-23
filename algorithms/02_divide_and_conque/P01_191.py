from typing import *


class Solution:
    def hammingWeight(self, target: int) -> int:
        if target < 2:
            return target
        return (target % 2) + self.hammingWeight(target // 2)
