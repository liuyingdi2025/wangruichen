from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.orders = None

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            # do something
            self.orders.append(node.val)
            # done
            self.inorder(node.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.orders = []
        self.inorder(root)
        min_differ = self.orders[-1] - self.orders[0]
        for index in range(1, len(self.orders)):
            min_differ = min(min_differ, self.orders[index] - self.orders[index - 1])
        return min_differ
