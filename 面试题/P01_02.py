from typing import *


class Solution:
    def to_dict(self, sequence):
        mydict = dict()
        for seq in sequence:
            if seq not in mydict:
                mydict[seq] = 0
            mydict[seq] += 1
        return mydict

    def CheckPermutation(self, sequence1: str, sequence2: str) -> bool:
        return self.to_dict(sequence1) == self.to_dict(sequence2)
