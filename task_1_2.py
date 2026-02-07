"""Задание «Проверка логина и пароля»"""


def check_auth(login: str, password: str):

    if (
        login == "admin" and password == "password"
    ):  # Здесь напишите свой код для проверки условия
        result = True
    else:
        result = False

    return result
