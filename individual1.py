#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_trains_info():
    """
    Функция запрашивает у пользователя информацию о поездах и возвращает список словарей поездов.
    """
    num_trains = int(input("Введите количество поездов: "))
    trains = []

    for _ in range(num_trains):
        destination = input("Введите название пункта назначения: ")
        train_number = input("Введите номер поезда: ")
        departure_time = input("Введите время отправления (в формате HH:MM): ")

        train = {
            'название пункта назначения': destination,
            'номер поезда': train_number,
            'время отправления': departure_time
        }
        trains.append(train)

    return trains


def sort_trains(trains):
    """
    Функция сортирует список поездов по названию пункта назначения.
    """
    return sorted(trains, key=lambda x: x['название пункта назначения'])


def display_sorted_trains(sorted_trains):
    """
    Функция выводит отсортированный список поездов на экран.
    """
    print("\nСписок поездов:")
    for train in sorted_trains:
        print(train)


def search_trains_by_time(sorted_trains):
    """
    Функция выполняет поиск поездов, отправляющихся после определенного времени.
    """
    search_time = input("\nВведите время для поиска поездов (в формате HH:MM): ")
    found_trains = [train for train in sorted_trains if train['время отправления'] > search_time]
    return found_trains


def display_found_trains(found_trains, search_time):
    """
    Функция выводит найденные поезда, отправляющиеся после определенного времени, на экран.
    """
    if found_trains:
        print("\nПоезда, отправляющиеся после {}: ".format(search_time))
        for train in found_trains:
            print(train)
    else:
        print("\nНет поездов, отправляющихся после {}".format(search_time))


def main():
    """
    Главная функция программы.
    """
    trains = get_trains_info()
    sorted_trains = sort_trains(trains)
    display_sorted_trains(sorted_trains)
    found_trains = search_trains_by_time(sorted_trains)
    display_found_trains(found_trains, search_time=input("Введите время для поиска: "))


if __name__ == "__main__":
    main()
