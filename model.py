def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')


def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')





def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Адрес", "Должность", "Кабинет"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Такой сотрудник отсутвует"


def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой сотрудник отсутвует"

def find_by_adress(data: list, adress: str) -> str:
    for el in data:
        if el.get("Адрес") == adress:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой сотрудник отсутвует"

def find_by_position(data: list, position: str) -> str:
    for el in data:
        if el.get("Должность") == position:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой сотрудник отсутвует"

def find_by_cabinet(data: list, cabinet: str) -> str:
    for el in data:
        if el.get("Кабинет") == cabinet:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой сотрудник отсутвует"


def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Адрес", "Должность", "Кабинет"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

