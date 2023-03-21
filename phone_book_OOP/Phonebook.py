import Contact as Cnt


class Phonebook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        result = '\n'
        for i, contact in enumerate(self.contacts, start=1):
            result += f'{i:<3}. {contact}\n'
        return result

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

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contacts(self, query: str):
        result = '\n'
        for i, contact in enumerate(self.contacts, start=1):
            if query in contact:
                result += f'{i:<3}. {contact}\n'
        return result

    def edit_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact
