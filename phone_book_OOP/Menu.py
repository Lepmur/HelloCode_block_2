class Menu:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def print_menu(self):
        print("1. Открыть книгу")
        print("2. Сохранить книгу")
        print("3. Вывести весь список контактов")
        print("4. Найти контакт")
        print("5. Редактировать контакт")
        print("6. Удалить контакт")
        print("7. Выход")

    def get_choice(self):
        choice = input("Выберите действие: ")
        return int(choice)

    def open_phonebook(self):
        filename = input("Введите имя файла: ") # открыть файл и сформировать список контактов | self.phonebook.contacts = ...

    def save_phonebook(self):
        filename = input("Введите имя файла: ") # записать список контактов в файл

    def print_contacts(self):
        for contact in self.phonebook.contacts:
            print("{} {} {} {}".format(contact.first_name, contact.last_name, contact.phone_number, contact.comment))

    def search_contacts(self):
        query = input("Введите запрос: ") # найти контакты по запросу и вывести их на экран

    def edit_contact(self):
        query = input("Введите запрос: ") # найти контакты по запросу | предложить выбрать контакт из найденных | запустить диалог редактирования контакта

    def delete_contact(self):
        query = input("Введите запрос: ") # найти контакты по запросу | предложить выбрать контакт из найденных | удалить контакт

    def run(self):
        while True:
            self.print_menu()
            choice = self.get_choice()
            if choice == 1:
                self.open_phonebook()
            elif choice == 2:
                self.save_phonebook()
            elif choice == 3:
                self.print_contacts()
            elif choice == 4:
                self.search_contacts()
            elif choice == 5:
                self.edit_contact()
            elif choice == 6:
                self.delete_contact()
            elif choice == 7:
                break
            else:
                print("Неверный выбор")