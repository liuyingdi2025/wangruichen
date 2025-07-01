from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def calc_depth(self, node, depth=1):
        if node is None:
            return True, depth
        left_flag, left_depth = self.calc_depth(node.left, depth + 1)
        right_flag, right_depth = self.calc_depth(node.right, depth + 1)
        if left_flag and right_flag:
            return abs(left_depth - right_depth) <= 1, max(left_depth, right_depth)
        else:
            return False, 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.calc_depth(root)[0]
