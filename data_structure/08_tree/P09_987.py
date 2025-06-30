from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def partition(items, left, right):
    pivot = left
    while left < right:
        # 从右向左，找到一个比 items[pivot] 更小的数
        while left <= right and items[pivot] <= items[right]:
            right -= 1
        if left <= right:
            items[pivot], items[right] = items[right], items[pivot]
            pivot = right
        # 从左向右，找到一个比 items[pivot] 更大的数
        while left <= right and items[left] < items[pivot]:
            left += 1
        if left <= right:
            items[left], items[pivot] = items[pivot], items[left]
            pivot = left
    return pivot


def quick_sort(items, left, right):
    pivot = partition(items, left, right)
    if left < pivot:
        quick_sort(items, left, pivot - 1)
    if pivot < right:
        quick_sort(items, pivot + 1, right)


class Triple:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def __lt__(self, t):
        if self.row < t.row:
            return True
        elif self.row > t.row:
            return False
        else:
            return self.value < t.value

    def __le__(self, t):
        if self.row < t.row:
            return True
        elif self.row > t.row:
            return False
        else:
            return self.value <= t.value

    def __gt__(self, t):  # self > t
        return not self <= t

    def __ge__(self, t):  # self > t
        return not self < t

    def __eq__(self, t):
        return self.row == t.row and self.value == t.value


class Solution:
    def __init__(self):
        self.mydict: Dict[int, List[Triple]] = dict()

    def traverse(self, node, row=0, column=0):
        if node is not None:
            if column not in self.mydict.keys():
                self.mydict[column] = list()
            self.mydict[column].append(Triple(row, column, node.val))
            self.traverse(node.left, row + 1, column - 1)
            self.traverse(node.right, row + 1, column + 1)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.traverse(root)
        ans = []
        for key in sorted(self.mydict.keys()):
            triples = self.mydict[key]
            quick_sort(triples, 0, len(triples) - 1)
            ans.append([_.value for _ in triples])
        return ans
