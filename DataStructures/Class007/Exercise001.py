from LinkedList import LinkedList


def main_menu():
    print("1 - Insert patient in the queue")
    print("2 - Show patients in the queue")
    print("3 - Call patient from teh queue")
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
    card_type = ''
    card_number = 0

    while True:
        card_type = input("Card color? (G or Y): ").upper()

        if not is_card_type_valid(card_type, CARD_TYPE_GREEN, CARD_TYPE_YELLOW):
            print("Invalid card type.")
            continue

        while True:
            card_number = int(input("Card number: "))

            if card_type == CARD_TYPE_GREEN:
                if is_card_number_valid(card_number, GREEN_CARD_MIN_VALUE, GREEN_CARD_MAX_VALUE):
                    break
            else:
                if is_card_number_valid(card_number, YELLOW_CARD_MIN_VALUE, YELLOW_CARD_MAX_VALUE):
                    break

            print("Invalid card number.")

        break

    print(f"Add patient card type {card_type} and card number {card_number}")


def show_patients():
    print("Show patients")


def call_patient():
    print("Call patient")


MAIN_MENU_MIN_VALUE = 1
MAIN_MENU_MAX_VALUE = 4
GREEN_CARD_MIN_VALUE = 1
GREEN_CARD_MAX_VALUE = 200
YELLOW_CARD_MIN_VALUE = 201
YELLOW_CARD_MAX_VALUE = 400
CARD_TYPE_GREEN = 'G'
CARD_TYPE_YELLOW = 'Y'

simple_list = LinkedList()

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
