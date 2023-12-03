#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_train(trains):
    """Добавляет информацию о поезде."""
    destination = input("Название пункта назначения: ")
    train_number = input("Номер поезда: ")
    departure_time = input("Время отправления (в формате ЧЧ:ММ): ")

    train = {
        'название пункта назначения': destination,
        'номер поезда': train_number,
        'время отправления': departure_time,
    }

    trains.append(train)
    trains.sort(key=lambda x: x['название пункта назначения'])


def list_trains(trains):
    """Выводит список всех поездов."""
    line = f'+-{"-" * 35}-+-{"-" * 15}-+-{"-" * 25}-+'
    print(line)
    print(f"| {'Название пункта назначения':^35} | {'Номер поезда':^15} | {'Время отправления':^25} |")

    for train in trains:
        print(line)
        print(
            f"| {train['название пункта назначения']:^35} | {train['номер поезда']:^15} | {train['время отправления']:^25} |")
    print(line)


def select_trains(trains, search_time):
    """Выводит поезда, отправляющиеся после указанного времени."""
    found = False
    result = []

    print(f"Поезда, отправляющиеся после {search_time}:")
    for train in trains:
        train_time = train['время отправления']
        if train_time >= search_time:
            result.append(train)
            found = True
    if found:
        return result

    if not found:
        return "Нет поездов, отправляющихся после указанного времени."


def display_help():
    """Выводит справку о доступных командах."""
    print("Список команд:\n")
    print("add - добавить информацию о поезде;")
    print("list - вывести список всех поездов;")
    print("select <время> - вывести поезда, отправляющиеся после указанного времени;")
    print("exit - завершить работу с программой.")


def main():
    """Основная функция управления программой."""
    trains = []

    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                break
            case 'add':
                add_train(trains)
            case 'list':
                list_trains(trains)
            case 'select':
                selected = select_trains(trains, input("Введите время для поиска поездов (в формате ЧЧ:ММ): "))
                list_trains(selected)
            case 'help':
                display_help()
            case _:
                print(f"Неизвестная команда {command}")


if __name__ == '__main__':
    main()
