from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.differ = -1

    def dfs(self, node, minimum, maximum):
        if node is not None:
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            if node.left is None and node.right is None:
                self.differ = max(self.differ, maximum - minimum)
            self.dfs(node.left, minimum, maximum)
            self.dfs(node.right, minimum, maximum)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root, root.val, root.val)
        return self.differ
