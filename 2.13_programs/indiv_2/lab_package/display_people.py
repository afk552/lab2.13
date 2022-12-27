def display_people(people_list):
    """
    Вывести людей из списка
    """
    if people_list:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 14,
            '-' * 19
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^14} | {:^19} |'.format(
                "№п/п",
                "Фамилия Имя",
                "Номер телефона",
                "Дата рождения"
            )
        )
        print(line)
        for nmbr, person in enumerate(people_list, 1):
            print(
                '| {:>4} | {:<30} | {:<14} | {:>19} |'.format(
                    nmbr,
                    person.get('name', ''),
                    person.get('pnumber', ''),
                    person.get('birth', '').strftime("%d.%m.%Y")
                )
            )
        print(line)
    else:
        print("Список людей пуст!")
