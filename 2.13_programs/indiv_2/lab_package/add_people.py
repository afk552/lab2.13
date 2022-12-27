import datetime as dt


def add_people():
    """
    Добавить людей
    """
    name = input("Введите фамилию и имя через пробел: ")
    pnumber = input("Введите номер телефона: ")
    birth = input("Введите дату рождения (01.01.2077): ").split('.')
    birth_dt = dt.datetime(int(birth[2]), int(birth[1]), int(birth[0]))
    return {
        'name': name,
        'pnumber': pnumber,
        'birth': birth_dt
    }
