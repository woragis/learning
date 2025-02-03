class Node:
    pass


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        value: int = self.value
        left: Node = self.left
        right: Node = self.right

    def __str__(self) -> str:
        return f"Node has:\nValue:{self.value}\nLeft: {self.left}\tRight: {self.right}"


class BinaryTree:
    tree = Node(2, Node(1), Node(3))

    def __init__(self):
        pass
