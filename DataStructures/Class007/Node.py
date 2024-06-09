class Node:
    def __init__(self, element=None):
        self.element = element
        self.next = None

    def __repr__(self):
        return self.element
