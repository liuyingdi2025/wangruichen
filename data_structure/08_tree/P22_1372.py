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
        self.maximum = 0

    def dfs(self, node, direction, count=0):
        """ the direction is the pointer: parent -> current node """
        if node is not None:
            if (direction == self.LEFT and node.right is None) or (direction == self.RIGHT and node.left is None):
                self.maximum = max(self.maximum, count)

            if direction == Solution.LEFT:
                self.dfs(node.left, Solution.LEFT, 1)
                self.dfs(node.right, Solution.RIGHT, count + 1)
            else:  # direction == Solution.RIGHT
                self.dfs(node.left, Solution.LEFT, count + 1)
                self.dfs(node.right, Solution.RIGHT, 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.dfs(root, Solution.LEFT, 0)
        self.dfs(root, Solution.RIGHT, 0)
        return self.maximum
