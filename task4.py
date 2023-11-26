#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    """
    Запрашивает ввод с клавиатуры и возвращает введенную строку.
    """
    user_input = input("Введите значение: ")
    return user_input


def test_input(value):
    """
    Проверяет, можно ли преобразовать значение к целому числу.
    Возвращает True, если можно, иначе - False.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def str_to_int(value):
    """
    Преобразует переданное значение к целому числу.
    Возвращает полученное число.
    """
    return int(value)


def print_int(value):
    """
    Выводит переданное значение на экран.
    """
    print(value)


def main():
    """
    Главная функция программы.
    """
    # Получаем ввод пользователя
    user_value = get_input()

    # Проверяем, можно ли преобразовать введенное значение к целому числу
    if test_input(user_value):
        # Если можно, преобразуем строку в целое число
        int_value = str_to_int(user_value)
        # Выводим полученное целое число на экран
        print_int(int_value)
    else:
        print("Невозможно преобразовать введенное значение в целое число.")


if __name__ == '__main__':
    main()
