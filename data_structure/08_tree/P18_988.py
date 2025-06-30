from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.path = chr(ord('z') + 1)

    def dfs(self, node, ancestors):
        if node is not None:
            ancestors = chr(node.val + ord('a')) + ancestors
            if node.left is None and node.right is None:
                if ancestors < self.path:
                    self.path = ancestors
            self.dfs(node.left, ancestors)
            self.dfs(node.right, ancestors)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root, '')
        return self.path
