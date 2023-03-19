import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('File opened successfully!')
            case 2:
                model.save_file()
                view.show_message('File saved successfully!')
            case 3:
                view.show_contacts(pb, 'Phonebook is empty or not open!')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Phonebook is empty or not open!'):
                    index = view.input_index('Enter information to search: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Contact {model.get_phone_book()[index - 1].get("name")} changed successfully!')
            case 6:
                search = view.input_search('Enter information to search: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Contact not found!')
            case 7:
                exit()
