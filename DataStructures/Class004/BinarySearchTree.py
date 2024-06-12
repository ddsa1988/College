class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.name < other.name

    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.name > other.name

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.name == other.name

        return False

    def __repr__(self):
        return f"Name: {self.name} CPF: {self.cpf}"


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


class BST:

    def __init__(self, key=None):
        self.root = key

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.__insert_node(self.root, key)

    def __insert_node(self, node, key):
        if not isinstance(node, Node):
            return

        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.__insert_node(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.__insert_node(node.right, key)


p1 = Person("Diego", 10)
p2 = Person("Amanda", 20)
p3 = Person("Rodrigo", 30)
p4 = Person("Caio", 40)
p5 = Person("Zeus", 50)

bst = BST()

bst.insert(p1)
bst.insert(p2)
bst.insert(p3)
bst.insert(p4)
bst.insert(p5)
