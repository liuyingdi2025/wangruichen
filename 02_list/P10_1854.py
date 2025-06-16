from typing import *


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mydict = dict()
        for log in logs:
            birth, depth = log[0], log[1]
            for year in range(birth, depth):
                if year not in mydict:
                    mydict[year] = 0
                mydict[year] += 1
        max_population = -1
        max_year = -1
        for year in sorted(mydict.keys()):
            if mydict[year] > max_population:
                max_population = mydict[year]
                max_year = year
        return max_year
