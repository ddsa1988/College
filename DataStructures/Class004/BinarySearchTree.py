from Node import Node


class BST:

    def __init__(self, key=None):
        self.__root = key

    def insert(self, key):
        if self.__root is None:
            self.__root = Node(key)
        else:
            self.__insert_node(self.__root, key)

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

    def in_order_traverse(self, callback):
        self.__in_order_traverse_node(self.__root, callback)

    def __in_order_traverse_node(self, node, callback):
        if node is not None:
            self.__in_order_traverse_node(node.left, callback)
            callback(node.key)
            self.__in_order_traverse_node(node.right, callback)
