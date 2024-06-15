from enum import Enum


class CardColor(Enum):
    GREEN = "V"
    YELLOW = "A"


class Card:
    def __init__(self, color, number):
        if isinstance(color, CardColor):
            self.color = color
            self.number = number
        else:
            raise TypeError("Color must be an instance of Direction Enum")

    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.color.value, self.number) == (other.color.value, other.number)

    def __repr__(self):
        return f"[{self.color.value}, {self.number}]"


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

            if current.element.color == CardColor.GREEN:
                node.next = current
                self.head = node

            else:
                previous = None

                while current is not None and (current.element.color != CardColor.GREEN):
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


def main_menu():
    print("1 - Insert patient in the queue")
    print("2 - Show patients in the queue")
    print("3 - Call patient from the queue")
    print("4 - Quit")


def is_card_type_valid(card, card_type1, card_type2):
    if not (isinstance(card, str) and isinstance(card_type1, str) and isinstance(card_type2, str)):
        return False

    return card.upper() == card_type1.upper() or card.upper() == card_type2.upper()


def is_card_number_valid(number, low, high):
    if not (isinstance(number, int) and isinstance(low, int) and isinstance(high, int)):
        return False

    return low <= number <= high


def get_main_menu_option(low, high):
    while True:
        try:
            user_input = int(input())
            if user_input < low or user_input > high:
                print(f"Invalid option: Must be from {low} to {high}.")
                continue
            return user_input
        except Exception as error:
            print(f"Invalid option: {type(error).__name__}")


def add_patient():
    while True:
        card_type = input(f"Card color? ({CardColor.GREEN.value} or {CardColor.YELLOW.value}): ").upper()

        if not is_card_type_valid(card_type, CardColor.GREEN.value, CardColor.YELLOW.value):
            print("Invalid card type.")
            continue

        while True:
            card_number = int(input("Card number: "))

            if card_type == CardColor.GREEN.value:
                if is_card_number_valid(card_number, GREEN_CARD_MIN_VALUE, GREEN_CARD_MAX_VALUE):
                    card = Card(CardColor.GREEN, card_number)
                    simple_list.insert_without_priority(card)
                    break
            else:
                if is_card_number_valid(card_number, YELLOW_CARD_MIN_VALUE, YELLOW_CARD_MAX_VALUE):
                    card = Card(CardColor.YELLOW, card_number)
                    simple_list.insert_with_priority(card)
                    break

            print("Invalid card number.")

        break


def show_patients():
    if simple_list.is_empty():
        print("There are no patients in the queue")
    else:
        print(f"List -> {simple_list}")


def call_patient():
    if simple_list.is_empty():
        print("There are no patients in the queue.")
    else:
        node = simple_list.remove()
        print(f"Calling patient card color {node.element.color.value} and number {node.element.number}")


MAIN_MENU_MIN_VALUE = 1
MAIN_MENU_MAX_VALUE = 4
GREEN_CARD_MIN_VALUE = 1
GREEN_CARD_MAX_VALUE = 200
YELLOW_CARD_MIN_VALUE = 201
YELLOW_CARD_MAX_VALUE = 400

simple_list = SimpleLinkedList()

while True:
    main_menu()
    user_option = get_main_menu_option(MAIN_MENU_MIN_VALUE, MAIN_MENU_MAX_VALUE)

    match user_option:
        case 1:
            add_patient()
        case 2:
            show_patients()
        case 3:
            call_patient()
        case 4:
            break
