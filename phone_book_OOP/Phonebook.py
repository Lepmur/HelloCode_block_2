import Contact as Cnt


class Phonebook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        result = ''
        for i, contact in enumerate(self.contacts, start=1):
            result += f'{i:<2}| {contact}\n'
        return result[:-2]

    def open(self, path: str):
        self.contacts.clear()
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            self.contacts.append(Cnt.Contact(*contact.strip().split(';')))

    def save(self, path: str):
        data = '\n'.join(contact.to_str() for contact in self.contacts)
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def add_contact(self, last_name: str, first_name: str, phone_number: str, comment: str):
        self.contacts.append(Cnt.Contact(last_name, first_name, phone_number, comment))

    def remove_contact(self, index: int):
        self.contacts.pop(index)

    def search_contacts(self, query: str):
        result = '\n'
        for i, contact in enumerate(self.contacts, start=1):
            if query.lower() in contact.to_str().lower():
                result += f'{i:<2}| {contact}\n'
        return result

    def edit_contact(self, index: int, last_name: str, first_name: str, phone_number: str, comment: str):
        first_name = first_name if first_name != '' else self.contacts[index].first_name
        last_name = last_name if last_name != '' else self.contacts[index].last_name
        phone_number = phone_number if phone_number != '' else self.contacts[index].phone_number
        comment = comment if comment != '' else self.contacts[index].comment
        self.contacts[index] = Cnt.Contact(last_name, first_name, phone_number, comment)

