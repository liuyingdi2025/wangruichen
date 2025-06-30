from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.flag = True
        self.values = set()

    def preorder(self, node):
        if node is not None:
            self.values.add(node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.preorder(root)
        return len(self.values) <= 1
