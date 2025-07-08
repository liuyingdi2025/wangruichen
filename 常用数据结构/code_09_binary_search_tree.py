class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.add(value)

    def contains(self, value):
        def _contains(node):
            if node is None:
                return False
            if value < node.value:
                return _contains(node.left)
            elif value > node.value:
                return _contains(node.right)
            else:
                return True

        return _contains(self.root)

    def get(self, value):
        def _get(node):
            pass

        return _get(self.root)

    def add(self, value):
        def _add(node):
            pass

        _add(self.root)
        return self

    def remove(self, value):
        def _remove(node):
            pass

        _remove(self.root)
        return self

    def inorder(self):
        orders = []

        def _inorder(node):
            pass

        _inorder(self.root)
        return orders

    def display(self):
        def _display(node):
            pass


if __name__ == '__main__':
    bst = BinarySearchTree([9, 7, 15, 5, 8, 10, 23, 2, 6, 12, 35, 26])
