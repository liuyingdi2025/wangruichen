from typing import *


class Solution:
    def compare(self, ch1, ch2):
        num1, num2 = ord(ch1), ord(ch2)
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
        else:
            return 0

    def binary_search(self, letters, target, left, right):
        # print(letters[left:right + 1], left, right)
        if left > right:
            return letters[0]
        mid = (left + right) // 2
        if self.compare(letters[mid], target) < 0:
            return self.binary_search(letters, target, mid + 1, right)
        elif self.compare(letters[mid], target) > 0:
            if mid == left or self.compare(letters[mid - 1], target) < 0:
                return letters[mid]
            else:
                return self.binary_search(letters, target, left, mid - 1)
        else:  # self.compare(letters[mid], target) == 0
            if mid + 1 == len(letters):
                return letters[0]
            elif self.compare(target, letters[mid + 1]) < 0:
                return letters[mid + 1]
            else:
                return self.binary_search(letters, target, mid + 1, right)

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return self.binary_search(letters, target, 0, len(letters) - 1)


print(Solution().nextGreatestLetter(["c", "f", "j"], 'a'))
print(Solution().nextGreatestLetter(["c", "f", "j"], 'c'))
print(Solution().nextGreatestLetter(["x", "x", "y", "y"], 'z'))
print(Solution().nextGreatestLetter(["x", "x", "y", "y"], 'y'))
