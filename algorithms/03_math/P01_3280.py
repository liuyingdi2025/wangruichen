from typing import *


class Solution:
    def binary_base(self, number):
        if number < 2:
            return str(number)
        return self.binary_base(number // 2) + str(number % 2)

    def convertDateToBinary(self, date: str) -> str:
        return '-'.join([self.binary_base(int(_)) for _ in date.split('-')])


print(Solution().convertDateToBinary('2025-06-19'))
