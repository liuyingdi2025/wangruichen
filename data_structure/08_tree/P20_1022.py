from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.paths = []

    def calc(self, sequence):
        sequence = sequence[::-1]
        ans = 0
        for index in range(len(sequence)):
            ans += int(sequence[index]) * 2 ** index
        return ans

    def dfs(self, node, ancestors):
        if node is not None:
            ancestors += str(node.val)
            if node.left is None and node.right is None:
                self.paths.append(ancestors)
            self.dfs(node.left, ancestors)
            self.dfs(node.right, ancestors)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root, '')
        return sum([self.calc(_) for _ in self.paths])
