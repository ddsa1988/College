class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Key: {self.key}\nLeft: {self.left}\nRight: {self.right}"


class BST:
    pass


node = Node("Diego")
print(node)
