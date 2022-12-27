from lab_package.add_people import add_people
from lab_package.correct_date import correct_date
from lab_package.display_people import display_people
from lab_package.help_str import help_str
from lab_package.select_people import select_people
import sys


def main():
    people = []
    print("Программа запущена, введите help для просмотра команд!")

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            person = add_people()
            people.append(person)
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == "list":
            display_people(people)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            printed_month = parts[1]
            corrected_month = correct_date(printed_month)
            selected = select_people(people, corrected_month)
            if len(selected) > 0:
                display_people(selected)
            else:
                print("Людей, чьи дни рождения приходятся на указанный месяц нет!")

        elif command == 'help':
            help_str()

        else:
            print(f"Неизвестная команда: {command}", file=sys.stderr)
