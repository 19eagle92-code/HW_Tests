"""Задание «Квадратное уравнение»"""


def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    # Ваш алгоритм
    return b**2 - 4 * a * c


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    D = discriminant(a, b, c)
    if D > 0:
        x_1 = (-b + (D) ** 0.5) / (2 * a)
        x_2 = (-b - (D) ** 0.5) / (2 * a)
        return x_1, x_2
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


if __name__ == "__main__":
    solution(1, 8, 15)
    solution(1, -13, 12)
    solution(-4, 28, -49)
    solution(1, 1, 1)
