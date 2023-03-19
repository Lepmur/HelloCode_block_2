class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contacts(self, query):
        result = []
        for contact in self.contacts:
            if query in contact.first_name or query in contact.last_name or query in contact.phone_number or query in contact.comment:
                result.append(contact)
        return result

    def edit_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact
