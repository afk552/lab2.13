def correct_date(print_month):
    """
    Скорректировать номер месяца
    """
    month_by_text = {
        "январь": "01",
        "февраль": "02",
        "март": "03",
        "апрель": "04",
        "май": "05",
        "июнь": "06",
        "июль": "07",
        "август": "08",
        "сентябрь": "09",
        "октябрь": "10",
        "ноябрь": "11",
        "декабрь": "12",
    }
    if print_month.isalpha():
        print_month.lower()
        for key, value in month_by_text.items():
            if key == print_month:
                print_month = value
    if len(print_month) == 1:
        return "0" + print_month
    else:
        return print_month
