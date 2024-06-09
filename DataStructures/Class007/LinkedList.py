﻿from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, new_node):
        current = self.head

        if self.head is None:
            self.head = new_node

        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.count += 1

    def insert_at(self, element, index):
        if 0 <= index < self.size():
            node = Node(element)

            if index == 0:
                current = self.head
                node.next = current
                self.head = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node

            self.count += 1
            return True

        return False

    def remove_at(self, index):
        if 0 <= index < self.size():
            current = self.head

            if index == 0:
                self.head = current.next

            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next

            self.count -= 1
            return current.element

        return None

    def remove(self, node):
        index = self.index_of(node)
        return self.remove_at(index)

    def index_of(self, element):
        current = self.head

        for i in range(self.size()):
            if current.element == element:
                return i

            current = current.next

        return -1

    def get_element_at(self, index):
        if 0 <= index < self.size():
            current = self.head

            for i in range(index):
                current = current.next

            return current

        return None

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(current.element)
            current = current.next

        return "List => " + ", ".join(nodes)
