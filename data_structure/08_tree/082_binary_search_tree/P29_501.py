from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.mydict = dict()

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            # do something
            if node.val not in self.mydict:
                self.mydict[node.val] = 0
            self.mydict[node.val] += 1
            # done
            self.inorder(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        max_count = max(self.mydict.values())
        ans = []
        for key, value in self.mydict.items():
            if value == max_count:
                ans.append(key)
        return ans
