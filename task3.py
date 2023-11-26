#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply_until_zero():
    """
    Считывает числа с клавиатуры и перемножает их до ввода числа 0.
    Возвращает произведение введенных чисел.
    """
    result = 1
    while True:
        num = float(input("Введите число (для завершения введите 0): "))
        if num == 0:
            break
        result *= num
    return result


def main():
    """
    Главная функция программы.
    """
    product = multiply_until_zero()
    print(f"Произведение введенных чисел: {product}")


if __name__ == '__main__':
    main()
