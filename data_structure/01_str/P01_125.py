from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        target = ''
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                target += ch.lower()
        return target == target[::-1]
