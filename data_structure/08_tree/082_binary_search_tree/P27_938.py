from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.low = None
        self.high = None
        self.ans = 0

    def solve(self, node):
        if node is not None:
            if self.low <= node.val <= self.high:  # 符合条件
                self.ans += node.val
            if node.val <= self.low:  # 只需要检索当前节点的右子树
                self.solve(node.right)
            elif self.low < node.val < self.high:  # 需要检索左、右子树
                self.solve(node.left)
                self.solve(node.right)
            else:  # node.val >= self.high # 只需要检索当前节点的左子树
                self.solve(node.left)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.solve(root)
        return self.ans
