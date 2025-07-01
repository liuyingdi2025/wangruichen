from typing import *


class Solution:
    def minimumBoxes(self, apples: List[int], boxes: List[int]) -> int:
        count = sum(apples)
        boxes = sorted(boxes, reverse=True)
        capacity = 0
        for index in range(len(boxes)):
            capacity += boxes[index]
            if capacity >= count:
                return index + 1
        return 0


print(Solution().minimumBoxes(
    apples=[1, 3, 2], boxes=[4, 3, 1, 5, 2]
))
