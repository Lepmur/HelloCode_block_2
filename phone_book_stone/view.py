import text_fields


def main_menu() -> int:
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Select a menu item >>>  ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Enter a number from 1 to {length_menu}: ')


def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<15}'
                  f'{contact.get("comment"):<25}')
        return True


def add_contact() -> dict:
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    comment = input('Enter comment: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def input_index(message: str):
    return int(input(message))


def input_search(message: str):
    return input(message)


def change_contact(book: list[dict], index: int):
    print('Enter new information if you need to change it:')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}


def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))
