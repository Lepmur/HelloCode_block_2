class Menu:
    def __init__(self, phonebook):
        self.phonebook = phonebook

    def print_menu(self):
        print('''ГЛАВНОЕ МЕНЮ:
  1. Открыть книгу
  2. Сохранить книгу
  3. Вывести весь список контактов
  4. Найти контакт
  5. Редактировать контакт
  6. Удалить контакт
  0. Выход''')

    def get_choice(self):
        choice = input("Выберите действие >>> ")
        if choice.isdigit():
            return int(choice)

    def open_phonebook(self):
        self.phonebook.open(input("Введите имя файла: "))
        self.message_print("Файл успешно открыт!")

    def save_phonebook(self):
        if self.phonebook.__str__() != '\n':
            self.phonebook.save(input("Введите имя файла: "))
            self.message_print("Файл успешно сохранён!")
        else:
            self.message_print()

    def print_contacts(self):
        if self.phonebook.__str__() != '\n':
            print(self.phonebook.__str__())
        else:
            self.message_print()

    def search_contacts(self):
        if self.phonebook.__str__() != '\n':
            print(self.phonebook.search_contacts(input("Введите запрос: ")))
        else:
            self.message_print()

    def edit_contact(self):
        if self.phonebook.__str__() != '\n':
            query = input("Введите запрос: ")  # найти контакты по запросу | предложить выбрать контакт из найденных | запустить диалог редактирования контакта
        else:
            self.message_print()

    def delete_contact(self):
        if self.phonebook.__str__() != '\n':
            query = input("Введите запрос: ")  # найти контакты по запросу | предложить выбрать контакт из найденных | удалить контакт
        else:
            self.message_print()

    def message_print(self, message="Книга пуста или еще не открыта!"):
        print('-' * len(message))
        print(message)
        print('-' * len(message))

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
                    self.edit_contact()
                elif choice == 6:
                    self.delete_contact()
                elif choice == 0:
                    break
                else:
                    self.message_print("Неверный выбор! Выберите корректный пункт меню!")
            except FileNotFoundError:
                self.message_print("Такой файл не найден!")
