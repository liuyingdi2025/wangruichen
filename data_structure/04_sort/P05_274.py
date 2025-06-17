from typing import *


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # 6 5 3 1 0
        # 至少发表了 h 篇论文，并且至少有 h 篇论文被引用次数大于等于 h
        for idx in range(len(citations)):
            if citations[idx] < idx + 1:
                return idx
        return len(citations)


print(Solution().hIndex([3, 0, 6, 1, 5]))
