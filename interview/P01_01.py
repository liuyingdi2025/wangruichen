from typing import *


class Solution:
    def isUnique(self, sequence: str) -> bool:
        characters = list(sequence)
        return len(characters) == len(set(characters))
