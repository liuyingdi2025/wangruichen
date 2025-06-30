from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.numbers = [0 for _ in range(10)]
        self.count = 0

    def dfs(self, node):
        if node is not None:
            self.numbers[node.val] = 1 - self.numbers[node.val]
            if node.left is None and node.right is None:
                self.count += 1 if sum(self.numbers) < 2 else 0
            self.dfs(node.left)
            self.dfs(node.right)
            self.numbers[node.val] = 1 - self.numbers[node.val]

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.count
