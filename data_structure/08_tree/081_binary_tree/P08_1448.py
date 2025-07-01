from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, node, max_ancestor=None):
        if max_ancestor is None:
            max_ancestor = node.val
        count = 0
        if node.val >= max_ancestor:
            count += 1
        max_ancestor = max(max_ancestor, node.val)
        if node.left is not None and node.right is not None:
            return count + self.solve(node.left, max_ancestor) + self.solve(node.right, max_ancestor)
        elif node.left is not None:
            return count + self.solve(node.left, max_ancestor)
        elif node.right is not None:
            return count + self.solve(node.right, max_ancestor)
        else:  # both left and right are None
            return count

    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.solve(root)
