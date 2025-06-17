from typing import *


class Solution:
    def selection_sort(self, students, column):
        for idx in range(len(students)):
            max_idx = idx
            for k in range(idx + 1, len(students)):
                if students[k][column] > students[max_idx][column]:
                    max_idx = k
            students[idx], students[max_idx] = students[max_idx], students[idx]

    def sortTheStudents(self, scores: List[List[int]], column: int) -> List[List[int]]:
        self.selection_sort(scores, column)
        return scores


print(Solution().sortTheStudents([
    [10, 6, 9, 1],
    [7, 5, 11, 2],
    [4, 8, 3, 15]
], 2))
