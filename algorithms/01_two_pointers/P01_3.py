from typing import *


class Solution:
    def lengthOfLongestSubstring(self, text: str) -> int:
        max_length = 0
        left, right = 0, 0
        characters = set()
        for right in range(len(text)):
            character = text[right]
            while character in characters:
                characters.remove(text[left])
                left += 1
            characters.add(character)
            max_length = max(max_length, right - left + 1)
        return max_length


print(Solution().lengthOfLongestSubstring("abcdbdabcddbac"))
