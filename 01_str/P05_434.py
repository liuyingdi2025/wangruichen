from typing import List, Dict


class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        word = ''
        for index in range(0, len(s)):
            if s[index].isspace():
                if len(word) > 0:
                    count += 1
                word = ''
            else:
                word += s[index]
        if len(word) > 0:
            count += 1
        return count
