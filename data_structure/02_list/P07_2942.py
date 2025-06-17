from typing import *


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx in range(len(words)):
            if x in words[idx]:
                res.append(idx)
        return res
