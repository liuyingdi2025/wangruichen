from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.values = set()

    def dfs(self, node):
        if node is not None:
            self.values.add(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

    def numColor(self, root: TreeNode) -> int:
        self.dfs(root)
        return len(self.values)
