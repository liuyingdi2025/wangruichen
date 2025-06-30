from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.values = []

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.values.append(node.val)
            self.inorder(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.values
