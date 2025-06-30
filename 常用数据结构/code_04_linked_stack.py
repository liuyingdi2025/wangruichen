from code_01_singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        # Top | Head -> ... -> ... -> None | Bottom
        self.ll = LinkedList()

    def is_empty(self):
        return self.ll.head is None

    def not_empty(self):
        return not self.is_empty()

    def push(self, value):
        self.ll.add_first(value)

    def get(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        return self.ll.get_value(0)

    def pop(self):
        if self.is_empty():
            raise RuntimeError('stack is empty')
        return self.ll.remove_first()
