from typing import *


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Tree(Node):
    def __init__(self, root):
        super().__init__(root.val, root.children)
        self.root = root

    def size(self):
        def calc_size(node):
            if node is None:
                return 0
            counter = 0
            for child in node.children:
                counter += calc_size(child)
            return 1 + counter

        pointer = self.root
        return calc_size(pointer)

    def height(self):
        def calc_height(node):
            if node is None:
                return 0
            counter = 0
            for child in node.children:
                temp = calc_height(child)
                if temp > counter:
                    counter = temp
            return 1 + counter

        pointer = self.root
        return calc_height(pointer)

    def level_order(self):
        orders = []
        nodes = [self.root]
        while len(nodes) > 0:
            node = nodes.pop(0)
            orders.append(node.val)
            if len(node.children) > 0:
                nodes.extend(node.children)
        return orders

    def bfs(self):
        return self.level_order()

    def dfs(self):
        orders = []

        def calc_dfs(node):
            if node is not None:
                orders.append(node.val)
                for child in node.children:
                    calc_dfs(child)

        calc_dfs(self.root)
        return orders

    def display(self, count=8):
        def recursive_display(node, level):
            if node is not None:
                print(f'|{'-' * count * level} [{node.val}]')
                for child in node.children:
                    recursive_display(child, level + 1)

        recursive_display(self.root, 0)


node1 = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
node5 = Node(5, [])
node6 = Node(6, [])
node7 = Node(7, [])
node1.children.extend([node2, node3, node4])
node3.children.extend([node5, node6])
node5.children.extend([node7])

tree = Tree(node1)
tree.display()
print(tree.height())
print(tree.dfs())
