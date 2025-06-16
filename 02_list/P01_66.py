from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for idx in range(len(digits) - 1, 0, -1):
            if digits[idx] == 10:
                digits[idx] = 0
                digits[idx - 1] += 1
            else:
                break
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)  # insert(a, b)  我要在 a 的位置上，插入 b
        return digits
