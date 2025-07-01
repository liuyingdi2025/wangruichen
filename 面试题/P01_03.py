from typing import *


class Solution:
    def replaceSpaces(self, sequence: str, length: int) -> str:
        return sequence[:length].replace(' ', '%20')


print(Solution().replaceSpaces(sequence="Mr John Smith    ", length=13))
