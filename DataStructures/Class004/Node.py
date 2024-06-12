class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.key == other.key
        else:
            return False

    def __repr__(self):
        return f"Key: {self.key}\nLeft: {self.left}\nRight: {self.right}"
