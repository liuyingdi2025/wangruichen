from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.orders = []

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            # do something
            self.orders.append(node.val)
            # done
            self.inorder(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.orders[k - 1]
