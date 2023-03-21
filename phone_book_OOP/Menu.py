import Phonebook


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
        if choice.isdigit() and 0 < int(choice) < 8:
            return int(choice)
        else:
            print("Выберите корректный пункт меню!")

    def open_phonebook(self):
        path = input("Введите имя файла: ")
        Phonebook.Phonebook.open(path)

    def save_phonebook(self):
        filename = input("Введите имя файла: ")
        Phonebook.Phonebook.save(filename)
        print("Файл сохранён успешно!")

    def print_contacts(self):
        if Phonebook.Phonebook:
            print(Phonebook.Phonebook.__str__(Phonebook.Phonebook))
        else:
            print("Книга пуста или еще не открыта!")

    def search_contacts(self):
        query = input("Введите запрос: ")
        print(Phonebook.Phonebook.search_contacts(query))

    def edit_contact(self):
        query = input(
            "Введите запрос: ")  # найти контакты по запросу | предложить выбрать контакт из найденных | запустить диалог редактирования контакта

    def delete_contact(self):
        query = input(
            "Введите запрос: ")  # найти контакты по запросу | предложить выбрать контакт из найденных | удалить контакт

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
