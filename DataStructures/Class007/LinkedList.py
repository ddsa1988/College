from Node import Node
from CardColor import CardColor


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_without_priority(self, element):
        node = Node(element)
        current = self.head

        if self.head is None:
            self.head = node

        else:
            while current.next is not None:
                current = current.next
            current.next = node

        self.count += 1

    def insert_with_priority(self, element):
        if self.head is None:
            self.insert_without_priority(element)

        else:
            node = Node(element)
            current = self.head

            if current.element.color == CardColor.GREEN.value:
                node.next = current
                self.head = node

            else:
                previous = None

                while current is not None and (current.element.color != CardColor.GREEN.value):
                    previous = current
                    current = current.next

                previous.next = node
                node.next = current

            self.count += 1

    def remove(self):
        if self.is_empty():
            return None

        current = self.head
        self.head = current.next
        self.count -= 1

        return current

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def __repr__(self):
        if self.is_empty():
            return ""

        current = self.head
        nodes = []

        while current is not None:
            nodes.append(str(current.element))
            current = current.next

        return " ".join(nodes)
