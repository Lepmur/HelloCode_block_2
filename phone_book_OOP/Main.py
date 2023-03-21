import Menu
import Phonebook

try:
    phonebook = Phonebook.Phonebook()
    menu = Menu.Menu(phonebook)
    menu.run()
except FileNotFoundError:
    print('Такой файл не найден!')
