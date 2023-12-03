#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(radius):
    """
    Вычисляет площадь круга по заданному радиусу.
    """
    return math.pi * radius ** 2


def cylinder():
    """
    Вычисляет площадь боковой поверхности цилиндра или полную площадь цилиндра
    в зависимости от выбора пользователя.
    """
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    side_area = 2 * math.pi * radius * height
    full_area = side_area + 2 * circle(radius)

    choice = input("Хотите получить только площадь боковой поверхности? (yes/no): ").lower()

    match choice:
        case 'yes':
            print(f"Площадь боковой поверхности цилиндра: {side_area:.2f}")
        case 'no':
            print(f"Полная площадь цилиндра: {full_area:.2f}")
        case _:
            print("Некорректный ввод. Пожалуйста, введите 'yes' или 'no'.")

def main():
    """
    Главная функция программы.
    """
    cylinder()


if __name__ == '__main__':
    main()
