from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.value = None
        self.target = None

    def dfs(self, node, depth):
        if node is not None:
            if depth == self.target - 1:
                node.left = TreeNode(self.value, node.left, None)
                node.right = TreeNode(self.value, None, node.right)
            else:
                self.dfs(node.left, depth + 1)
                self.dfs(node.right, depth + 1)

    def addOneRow(self, root: Optional[TreeNode], value: int, target: int) -> Optional[TreeNode]:
        if target == 1:
            return TreeNode(value, root, None)
        self.value = value
        self.target = target
        self.dfs(root, 1)
        return root
