def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь список сотрудников\n"
          "2. Найти сотрудника по фамилии\n"
          "3. Найти сотрудника по номеру телефона\n"
          "4. Найти сотрудника по адресу\n"
          "5. Найти сотрудника по должности\n"
          "6. Найти сотрудника по кабинету\n"
          "7. Добавить сотрудника в список\n"
          "8. Сохранить список в текстовом формате\n"
          "9. Закончить работу")
    choice = int(input())
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)


def get_search_name() -> str:
    return input("Введите фамилию для поиска: ")

def get_search_number() -> str:
    return input("Введите номер телефона для поиска: ")

def get_search_adress() -> str:
    return input("Введите номер адрес сотрудника для поиска: ")

def get_search_position() -> str:
    return input("Введите должность сотрудника для поиска: ")
    
def get_search_cabinet() -> str:
    return input("Введите номер кабинета сотрудника для поиска: ")


def get_new_user() -> str:
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    adress = input("Введите адрес сотрудника: ")
    position = input("Введите должность сотрудника: ")
    cabinet = input("Введите кабинет сотрудника")
    return f'{last_name},{first_name},{phone_number},{adress},{position}, {cabinet}'

def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")
