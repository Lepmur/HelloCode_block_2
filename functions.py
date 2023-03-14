def menu(choices: []) -> int:
    print('\n'.join(choices))
    # return input('Ваш выбор >>> ')

def open_file(path: str) -> dict:
    data = {}
    with open(path, 'r', encoding='utf-8') as file:
        for i in file.read().split('\n'):
            name_number = i.split(';')
            if name_number != ['']:
                data[name_number[0]] = name_number[1]
    return data

def save(path: str, data: {}):
    with open(path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write('{};{}\n'.format(item, data[item]))

def show(data: {}):
    count = 1
    for item in sorted(data):
        print(f'{count}. {item} {data[item]}')
        count += 1

def find(data: {}, find_object: str) -> {}:
    result = {}
    for item in data:
        if find_object.lower() in str(item).lower() or find_object in str(data[item]).lower():
            result[item] = data[item]
    return result

def add(data: {}, add_second_name: str, add_first_name: str, add_number: str):
    key = f'{add_second_name} {add_first_name}'
    data[key] = f'{add_number}'

def edit_find(data: {}, edit_object: str) -> str:
    found = find(data, edit_object)
    if len(found) > 1:
        show(found)
        number_for_edit = int(input('Узнаёшь кого то из них? Назови номер, они тебя не видят: '))
        count = 0
        for item in sorted(found):
            count += 1
            if count == number_for_edit:
                 return item
    elif len(found) == 1:
        for item in found:
            return item

def delete(data: {}, key_in_base: str):
    del data[key_in_base]





