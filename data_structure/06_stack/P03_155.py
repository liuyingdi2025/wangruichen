class Node:
    def __init__(self, value, minimum):
        self.value = value
        self.minimum = minimum


class MinStack:
    def __init__(self):
        self.nodes = []

    def push(self, val: int) -> None:
        if len(self.nodes) == 0:
            self.nodes.append(Node(val, val))
        else:
            self.nodes.append(Node(val, min(self.nodes[-1].minimum, val)))

    def pop(self) -> None:
        self.nodes = self.nodes[:-1]

    def top(self) -> int:
        return self.nodes[-1].value

    def getMin(self) -> int:
        return self.nodes[-1].minimum
