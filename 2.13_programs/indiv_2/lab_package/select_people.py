def select_people(people_list, correct_printed_month):
    """
    Выбрать людей по заданному месяцу рождения
    """
    result = []
    for person in people_list:
        birth = person.get('birth')
        if correct_printed_month == birth.strftime("%m"):
            result.append(person)
    return result
