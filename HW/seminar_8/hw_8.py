# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.

def enter_first_name():
    return input("ВВедите имя: ")


def enter_second_name():
    return input("ВВедите отчество: ")


def enter_family_name():
    return input("ВВедите фамилию: ")


def enter_phone_number():
    return input("ВВедите номер телефона: ")


def enter_address_number():
    return input("ВВедите адрес абонента: ")


def enter_data():
    name = enter_first_name().title()
    surname = enter_second_name().title()
    family = enter_family_name().title()
    number = enter_phone_number()
    address = enter_address_number().title()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def search_line():
    print('Выберите вариант поиска: \n'
          '1. Имя\n'
          '2. Отчество\n'
          '3. Фамилия\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите номер варианта: ')) - 1
    searched = input('Введите параметр поиска: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            contact = item.replace('\n', ' ').split()
            if searched in contact[index]:
                print(item)

            # file.seek(0)
            # print(file.readlines())


def delete_item():
    with open('book.txt', 'r', encoding="utf-8") as file:
        X = input('Введите параметр поиска: ').title()
        lines = file.read().strip().split('\n\n')
        with open('book.txt', 'w', encoding="utf-8") as file:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    file.write(f'{line.strip()}\n\n')


def edit_item():
    with open('book.txt', 'r', encoding="utf-8") as file:
        X = input('Введите параметр поиска: ').title()
        lines = file.read().strip().split('\n\n')
        with open('book.txt', 'w', encoding="utf-8") as file:
            for line in lines:
                if X in line:
                    name = enter_first_name().title()
                    surname = enter_second_name().title()
                    family = enter_family_name().title()
                    number = enter_phone_number()
                    address = enter_address_number().title()
                    line = f'{name} {surname} {family}\n{number}\n{address}\n\n'
                    file.write(f'{line.strip()}\n\n')
                else:
                    file.write(f'{line.strip()}\n\n')


def interface():
    cmd = 0
    while cmd != '4':
        print('Выберите действие: \n'
              '1. Добавить контакт: \n'
              '2. Вывести все контакты: \n'
              '3. Поиск контакта: \n'
              '4. Удалить контакт: \n'
              '5. Изменить контакт: \n'
              '6. Выход: '
              )

        cmd = input('Введите действие: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Не корректный ввод.')
            cmd = input('Введите действие: ')
        match cmd:
            case '1': enter_data()
            case '2': print_data()
            case '3': search_line()
            case '4': delete_item()
            case '5': edit_item()
            case '6': print('Работа программы завершена.')


interface()
