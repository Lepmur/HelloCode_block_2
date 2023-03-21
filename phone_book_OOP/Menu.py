import Contact


class Menu:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def print_menu(self):
        print('''ГЛАВНОЕ МЕНЮ:
  1. Открыть книгу
  2. Сохранить книгу
  3. Вывести весь список контактов
  4. Найти контакт
  5. Добавить контакт
  6. Редактировать контакт
  7. Удалить контакт
  0. Выход''')

    def get_choice(self):
        choice = input("Выберите действие >>> ")
        if choice.isdigit():
            return int(choice)

    def open_phonebook(self):
        path = input("Введите имя файла: ")
        if path != '':
            self.phonebook.open(path)
            self.message_print("Файл успешно открыт!")
        else:
            self.message_print("Это поле не может быть пустым!")

    def save_phonebook(self):
        if self.phonebook.__str__() != '':
            self.phonebook.save(input("Введите имя файла: "))
            self.message_print("Файл успешно сохранён!")
        else:
            self.message_print()

    def print_contacts(self):
        if self.phonebook.__str__() != '':
            self.message_print(self.phonebook.__str__())
        else:
            self.message_print()

    def search_contacts(self):
        if self.phonebook.__str__() != '':
            answer = self.phonebook.search_contacts(input("Введите искомый контакт: "))
            if answer != '':
                self.message_print(answer)
            else:
                self.message_print("Ничего не найдено!")
        else:
            self.message_print()

    def add_contact(self):
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        comment = input("Введите комментарий: ")
        self.phonebook.add_contact(last_name, first_name, phone_number, comment)
        self.message_print("Контакт добавлен успешно!")

    def edit_contact(self):
        if self.phonebook.__str__() != '':
            self.print_contacts()
            index = input("Введите номер контакта для редактирования: ")
            if index.isdigit() and 0 < int(index) < len(self.phonebook.contacts):
                last, first = Contact.Contact.to_str(self.phonebook.contacts[int(index) - 1]).split(';')[:2]
                self.message_print(f"Редактируем контакт {last} {first}!")
                last_name = input("Введите новую фамилию или Enter для пропуска поля: ")
                first_name = input("Введите новое имя или Enter для пропуска поля: ")
                phone_number = input("Введите новый номер телефона или Enter для пропуска поля: ")
                comment = input("Введите новый комментарий или Enter для пропуска поля: ")
                self.phonebook.edit_contact(int(index) - 1, last_name, first_name, phone_number, comment)
                self.message_print("Контакт успешно изменён!")
            else:
                self.message_print("Такого контакта нет!")
        else:
            self.message_print()

    def delete_contact(self):
        if self.phonebook.__str__() != '':
            self.print_contacts()
            index = input("Введите номер контакта для удаления: ")
            if index.isdigit() and 0 < int(index) < len(self.phonebook.contacts):
                last, first = Contact.Contact.to_str(self.phonebook.contacts[int(index) - 1]).split(';')[:2]
                self.phonebook.remove_contact(int(index) - 1)
                self.message_print(f"Контакт {last} {first} успешно удалён!")
            else:
                self.message_print("Такого контакта нет!")
        else:
            self.message_print()

    def message_print(self, message="Книга пуста или еще не открыта!"):
        length = len(message)
        if length > 60:
            length = 55
        print('-' * length)
        print(message)
        print('-' * length)

    def run(self):
        while True:
            try:
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
                    self.add_contact()
                elif choice == 6:
                    self.edit_contact()
                elif choice == 7:
                    self.delete_contact()
                elif choice == 0:
                    break
                else:
                    self.message_print("Неверный выбор! Выберите корректный пункт меню!")
            except FileNotFoundError:
                self.message_print("Такой файл не найден!")
