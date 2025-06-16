from typing import List, Dict


class Solution:
    def replace(self, word: str, index: int, target: str) -> str:
        return word[:index] + target + word[index + 1:]

    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    s = self.replace(s, right, s[left])
                else:
                    s = self.replace(s, left, s[right])
            left += 1
            right -= 1
        return s
