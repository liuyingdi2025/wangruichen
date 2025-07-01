from typing import *


class Solution:
    def canPermutePalindrome(self, sequence: str) -> bool:
        myset = set()
        for seq in sequence:
            if seq not in myset:
                myset.add(seq)
            else:
                myset.remove(seq)
        return len(myset) < 2
