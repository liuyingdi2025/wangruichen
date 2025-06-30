from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, node: TreeNode, sum_ancestors: int, target: int) -> bool:
        if node.left is not None and node.right is not None:
            return self.solve(node.left, sum_ancestors + node.val, target) or self.solve(node.right, sum_ancestors + node.val, target)
        if node.left is None and node.right is None:
            return sum_ancestors + node.val == target
        if node.left is not None:
            return self.solve(node.left, sum_ancestors + node.val, target)
        if node.right is not None:
            return self.solve(node.right, sum_ancestors + node.val, target)

    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if root is None:
            return False
        return self.solve(root, 0, target)
