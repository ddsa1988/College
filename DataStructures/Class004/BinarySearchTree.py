class Node:
    def __init__(self, element=None):
        self.element = element
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Element: {self.element}\nLeft: {self.left}\nRight: {self.right}"


class BST:
    pass


node = Node("Diego")
print(node)
