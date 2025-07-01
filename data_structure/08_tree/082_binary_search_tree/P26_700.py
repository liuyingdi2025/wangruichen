from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target = None

    def solve(self, node):
        if node is None:
            return None
        if self.target < node.val:
            return self.solve(node.left)
        elif self.target > node.val:
            return self.solve(node.right)
        else:
            return node

    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.target = target
        return self.solve(root)
