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
            self.orders.append(node.val)
            self.inorder(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.orders = []
        self.inorder(root)
        for index in range(1, len(self.orders)):
            if self.orders[index - 1] >= self.orders[index]:
                return False
        return True
