from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calc_min_depth(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return 1 + self.calc_min_depth(node.right)
        if node.right is None:
            return 1 + self.calc_min_depth(node.left)
        return 1 + min(self.calc_min_depth(node.left), self.calc_min_depth(node.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.calc_min_depth(root)
