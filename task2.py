import math

def circle(radius):
    """
    Вычисляет площадь круга по заданному радиусу.
    """
    return math.pi * radius ** 2

def cylinder():
    """
    Вычисляет площадь боковой поверхности цилиндра или полную площадь цилиндра
    в зависимости от выбора пользователя, используя match.
    """
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    side_area = 2 * math.pi * radius * height
    full_area = side_area + 2 * circle(radius)

    choice = input("Хотите получить только площадь боковой поверхности? (yes/no): ").lower()
    
    result = match choice:
        case 'yes':
            f"Площадь боковой поверхности цилиндра: {side_area:.2f}"
        case 'no':
            f"Полная площадь цилиндра: {full_area:.2f}"
        case _:
            "Некорректный ввод. Пожалуйста, введите 'yes' или 'no'."

    print(result)

def main():
    """
    Главная функция программы.
    """
    cylinder()

if __name__ == '__main__':
    main()
