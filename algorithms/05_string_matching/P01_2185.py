from typing import *


class Solution:
    def __init__(self):
        self.words = []
        self.prefix = ''

    def count(self, index=0):
        if index >= len(self.words):
            return 0
        return (1 if self.words[index].startswith(self.prefix) else 0) + self.count(index + 1)

    def prefixCount(self, words: List[str], prefix: str) -> int:
        self.words = words
        self.prefix = prefix
        return self.count()


print(Solution().prefixCount(
    words=["leetcode", "win", "loops", "success"],
    prefix="code"
))
