import functions as f
# from termcolor import colored, cprint

data = {}
path = ''
choices = ('1 - Открыть файл телефонной книги', '2 - Сохранить книгу в файл', '3 - Показать все контакты',
           '4 - Найти контакт', '5 - Добавить контакт', '6 - Изменить контакт', '7 - Удалить контакт', '0 - Выход')
f.menu(choices)
while True:
    if path != '':
        print(f'Работаю с книгой: {path}. Посмотреть меню - 9.')
    else:
        print('Никакой файл не открыт! Посмотреть меню - 9.')
    try:
        # choice = int(f.menu(choices))
        choice = int(input('Ваш выбор >>> '))
        if choice == 0:
            if data != {}:
                if input('Кто-то из нас не сохранился, точно закрываю? (YES): ').lower() == 'yes':
                    exit()
            else:
                exit()
        elif choice == 1: # open
            path = input('Какой мне файл открыть?: ')
            try:
                data = f.open_file(path)
            except FileNotFoundError:
                print('Я не могу найти такой файл!')
                path = ''
        elif choice == 2: # save
            if data != {}:
                if path != '' and input(f'Перезапишу этот файл? ({path}) (YES): ').lower() == 'yes':
                    f.save(path, data)
                else:
                    path = input('А куда сохранить?: ')
                    f.save(path, data)
                path = ''
                data.clear()
            else:
                print('Мне пока нечего сохранять...')
        elif choice == 3: # look contacts
            if data != {}:
                f.show(data)
            else:
                print('Нечего мне показывать')
        elif choice == 4: # find contact
            if data != {}:
                find_object = input('Что мне найти? ').lower()
                found_contacts = f.find(data, find_object)
                if found_contacts != {}:
                    f.show(found_contacts)
                else:
                    print('Я не нашёл такой контакт :-(')
            else:
                print('Негде мне искать')
        elif choice == 5: # add contact
            if data != {}:
                add_second_name = input('Введи фамилию: ')
                add_first_name = input('Введи имя: ')
                add_number = input('Введи номер: ')
                f.add(data, add_second_name, add_first_name, add_number)
            else:
                print('Я не знаю куда добавлять')
        elif choice == 6: # edit
            if data != {}:
                edit_contact = f.edit_find(data, input('Кого будем редактировать? '))
                if edit_contact is not None:
                    print(f'Редактируем {edit_contact} {data[edit_contact]}')
                    add_second_name = input('Введи новую фамилию: ')
                    add_first_name = input('Введи новое имя: ')
                    add_number = input('Введи новый номер: ')
                    f.add(data, add_second_name, add_first_name, add_number)
                    f.delete(data, edit_contact)
                else:
                    print('Я не нашёл такой контакт :-(')
            else:
                print('Менять пока нечего')
        elif choice == 7: # delete
            if data != {}:
                delete_contact = f.edit_find(data, input('Кого мне ликвидировать? '))
                if delete_contact is not None:
                    print(f'Удаляем {delete_contact} {data[delete_contact]}')
                    f.delete(data, delete_contact)
                else:
                    print('Я не нашёл такой контакт :-(')
            else:
                print('Что мертво умереть не может!')
        elif choice == 9: # menu
            f.menu(choices)
        else:
            print(f'Я не вижу тут варианта {choice}, уж извиняй')
    except ValueError:
        print('По-моему тут надо ввести цифру... но тебе конечно виднее')
