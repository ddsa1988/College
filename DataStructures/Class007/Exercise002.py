def hash_func_digits(key, size, default="DF"):
    if not (isinstance(key, str) and isinstance(default, str) and isinstance(size, int)):
        return -1

    if len(key) != 2:
        return -1

    if key.upper() == default.upper():
        return 7

    return (ord(key[0].upper()) + ord(key[1].upper())) % size


class State:
    def __init__(self, name, acronym):
        self.name = name
        self.acronym = acronym

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.acronym == other.acronym

        return False

    def __repr__(self):
        return self.acronym


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def __repr__(self):
        return self.element


class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, element):
        new_node = Node(element)
        current = self.head

        if self.head is None:
            self.head = new_node

        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.count += 1

    def insert_at(self, element, index):
        if (0 <= index < self.size()) or index == 0:
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
            return current.key

        return None

    def remove(self, element):
        index = self.index_of(element)
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
        if self.is_empty():
            return ""

        current = self.head
        nodes = []

        while current is not None:
            nodes.append(str(current.element))
            current = current.next

        nodes.append(str(current))

        return " -> ".join(nodes)


class Table:
    def __init__(self, size):
        self.table = [None] * abs(size)

    def insert(self, element):
        if isinstance(element, State):
            pos = hash_func_digits(element.acronym, len(self.table))

            if 0 <= pos < len(self.table):
                if self.table[pos] is None:
                    simple_list = SimpleLinkedList()
                    simple_list.push(element)
                    self.table[pos] = simple_list

                else:
                    simple_list = self.table[pos]
                    if isinstance(simple_list, SimpleLinkedList):
                        if simple_list.index_of(element) == -1:
                            simple_list.insert_at(element, 0)

    def __repr__(self):
        string = ""

        for i in range(len(self.table)):
            string += f"{i}: {self.table[i]}\n"

        return string


table = Table(10)
print(table)
print()

table.insert(State("Acre", "AC"))
table.insert(State("Alagoas", "AL"))
table.insert(State("Amapa", "AP"))
table.insert(State("Amazonas", "AM"))
table.insert(State("Bahia", "BA"))
table.insert(State("Ceara", "CE"))
table.insert(State("Distrito Federal", "DF"))
table.insert(State("Espirito Santo", "ES"))
table.insert(State("Goias", "GO"))
table.insert(State("Maranhao", "MA"))
table.insert(State("Mato Grosso", "MT"))
table.insert(State("Mato Grosso do Sul", "MS"))
table.insert(State("Minas Gerais", "MG"))
table.insert(State("Para", "PA"))
table.insert(State("Paraiba", "PB"))
table.insert(State("Parana", "PR"))
table.insert(State("Pernambuco", "PE"))
table.insert(State("Piaui", "PI"))
table.insert(State("Rio de Janeiro", "RJ"))
table.insert(State("Rio Grande do Norte", "RN"))
table.insert(State("Rio Grande do Sul", "RS"))
table.insert(State("Rondonia", "RO"))
table.insert(State("Roaraima", "RR"))
table.insert(State("Santa Catarina", "SC"))
table.insert(State("Sao Paulo", "SP"))
table.insert(State("Sergipe", "SE"))
table.insert(State("Tocantins", "TO"))

print(table)
print()

table.insert(State("Diego Alexandre", "DA"))
print(table)
