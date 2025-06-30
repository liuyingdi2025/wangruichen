from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    def __init__(self):
        self.ans = 0

    def dfs(self, node, direction=''):
        if node is not None:
            if node.left is None and node.right is None and direction == Solution.LEFT:
                self.ans += node.val
            self.dfs(node.left, Solution.LEFT)
            self.dfs(node.right, Solution.RIGHT)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans
