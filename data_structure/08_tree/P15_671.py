from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.items = set()

    def dfs(self, node):
        if node is not None:
            self.items.add(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        self.items = sorted(list(self.items))
        return self.items[1] if len(self.items) > 1 else -1
