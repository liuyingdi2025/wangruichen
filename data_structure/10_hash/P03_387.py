from typing import *


class Solution:
    def firstUniqChar(self, text: str) -> int:
        mydict = dict()
        for ch in text:
            if ch not in mydict:
                mydict[ch] = 0
            mydict[ch] += 1
        for idx in range(len(text)):
            if mydict[text[idx]] == 1:
                return idx
        return -1
