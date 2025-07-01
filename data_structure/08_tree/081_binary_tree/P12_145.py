from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, values):
        if node is not None:
            if node.left is None and node.right is None:
                values.append(node.val)
            self.dfs(node.left, values)
            self.dfs(node.right, values)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        values1, values2 = [], []
        self.dfs(root1, values1)
        self.dfs(root2, values2)
        return values1 == values2
