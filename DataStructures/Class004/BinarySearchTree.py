from Node import Node


class BST:

    def __init__(self):
        self.__root = None

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

    def pre_order_traverse(self, callback):
        self.__pre_order_traverse_node(self.__root, callback)

    def __pre_order_traverse_node(self, node, callback):
        if node is not None:
            callback(node.key)
            self.__pre_order_traverse_node(node.left, callback)
            self.__pre_order_traverse_node(node.right, callback)

    def post_order_traverse(self, callback):
        self.__post_order_traverse_node(self.__root, callback)

    def __post_order_traverse_node(self, node, callback):
        if node is not None:
            self.__post_order_traverse_node(node.left, callback)
            self.__post_order_traverse_node(node.right, callback)
            callback(node.key)

    def min(self):
        return self.__min_value(self.__root)

    def __min_value(self, node):
        current = node

        while current is not None and current.left is not None:
            current = current.left

        return current.key

    def max(self):
        return self.__max_value(self.__root)

    def __max_value(self, node):
        current = node

        while current is not None and current.right is not None:
            current = current.right

        return current.key

    def search(self, key):
        return self.__search_node(self.__root, key)

    def __search_node(self, node, key):
        if node is None:
            return False

        if not isinstance(key, type(node.key)):
            return False

        if key < node.key:
            return self.__search_node(node.left, key)
        elif key > node.key:
            return self.__search_node(node.right, key)
        else:
            return True

    def remove(self, key):
        self.__root = self.__remove_node(self.__root, key)

    def __remove_node(self, node, key):
        if node is None:
            return None

        if not isinstance(key, type(node.key)):
            return None

        if key < node.key:
            node.left = self.__remove_node(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove_node(node.right, key)
            return node
        else:
            if node.left is None and node.right is None:
                node = None
                return node

            if node.left is None:
                node = node.right
                return node

            elif node.right is None:
                node = node.left
                return node

            aux = self.__min_node(node.right)
            node.key = aux.key
            node.right = self.__remove_node(node.right, aux.key)
            return node

    def __min_node(self, node):
        current = node

        while current is not None and current.left is not None:
            current = current.left

        return current
