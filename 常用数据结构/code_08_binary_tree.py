from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(TreeNode):
    def __init__(self, param):
        if isinstance(param, TreeNode):
            super().__init__(param.val, param.left, param.right)
            self.root = param
        elif isinstance(param, list):
            nodes = [TreeNode(_) if _ is not None else None for _ in param]
            for index in range(len(nodes)):
                if nodes[index] is not None:
                    if index * 2 + 1 < len(nodes):
                        nodes[index].left = nodes[index * 2 + 1]
                    if index * 2 + 2 < len(nodes):
                        nodes[index].right = nodes[index * 2 + 2]
            self.root = nodes[0]
        else:
            raise TypeError('the type of the initial parameter is incorrect')

    def size(self):
        def calc_size(node):
            if node is None:
                return 0
            return 1 + calc_size(node.left) + calc_size(node.right)

        pointer = self.root
        return calc_size(pointer)

    def height(self):
        def calc_height(node):
            if node is None:
                return 0
            return 1 + max(calc_height(node.left), calc_height(node.right))

        pointer = self.root
        return calc_height(pointer)

    def level_order(self):
        orders = []
        nodes = [self.root]
        while len(nodes) > 0:
            node = nodes.pop(0)
            orders.append(node.val)
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)
        return orders

    def preorder(self):
        orders = []

        def calc_preorder(node):
            if node is not None:
                orders.append(node.val)
                calc_preorder(node.left)
                calc_preorder(node.right)

        calc_preorder(self.root)
        return orders

    def inorder(self):
        orders = []

        def calc_inorder(node):
            if node is not None:
                calc_inorder(node.left)
                orders.append(node.val)
                calc_inorder(node.right)

        calc_inorder(self.root)
        return orders

    def postorder(self):
        orders = []

        def calc_postorder(node):
            if node is not None:
                calc_postorder(node.left)
                calc_postorder(node.right)
                orders.append(node.val)

        calc_postorder(self.root)
        return orders

    def bfs(self):
        return self.level_order()

    def dfs(self):
        return self.preorder()

    def to_list(self):
        if self.root is None:
            return []
        nodes: List[Optional[TreeNode]] = [None for _ in range(2 ** self.height() - 1)]
        nodes[0] = self.root
        for index in range(1, len(nodes), 2):
            parent = nodes[(index - 1) // 2]
            if parent is not None:
                nodes[index] = parent.left
                nodes[index + 1] = parent.right
        return [_.val if _ is not None else None for _ in nodes]

    def display(self, count=8):
        def recursive_display(node, level, prefix='Root'):
            if node is not None:
                print(f'|{'-' * count * level} {prefix}:[{node.val}]')
                recursive_display(node.left, level + 1, 'L')
                recursive_display(node.right, level + 1, 'R')

        recursive_display(self.root, 0)
