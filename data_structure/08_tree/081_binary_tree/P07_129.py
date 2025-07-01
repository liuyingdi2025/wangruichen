from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.numbers = []

    def solve(self, node, ancestors):
        if node.left is not None and node.right is not None:
            self.solve(node.left, ancestors + str(node.val))
            self.solve(node.right, ancestors + str(node.val))
        elif node.left is not None:
            self.solve(node.left, ancestors + str(node.val))
        elif node.right is not None:
            self.solve(node.right, ancestors + str(node.val))
        else:  # both left and right are None
            self.numbers.append(ancestors + str(node.val))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.solve(root, '0')
        return sum([int(_) for _ in self.numbers])
