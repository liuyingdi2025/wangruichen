from typing import *


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for idx in range(1, len(height)):
            if height[idx - 1] > threshold:
                res.append(idx)
        return res
