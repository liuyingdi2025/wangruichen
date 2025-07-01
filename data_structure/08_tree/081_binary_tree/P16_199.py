from typing import *


class Queue:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return len(self.values) == 0

    def enqueue(self, value):
        self.values.append(value)
        return self

    def enqueue_batch(self, values):
        self.values.extend(values)
        return self

    def dequeue(self):
        value = self.values[0]
        self.values = self.values[1:]
        return value

    def front(self):
        return self.values[0]

    def traverse(self):
        print(' <- '.join([str(_) for _ in self.values]))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.mydict = dict()

    def bfs(self, root):
        queue = Queue().enqueue((root, 1))
        while not queue.is_empty():
            node, level = queue.dequeue()
            if level not in self.mydict:
                self.mydict[level] = []
            self.mydict[level].append(node.val)
            if node.left is not None:
                queue.enqueue((node.left, level + 1))
            if node.right is not None:
                queue.enqueue((node.right, level + 1))

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.bfs(root)
        ans = []
        for depth in sorted(self.mydict.keys()):
            ans.append(self.mydict[depth][-1])
        return ans
