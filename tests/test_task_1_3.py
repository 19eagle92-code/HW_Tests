import unittest

from task_1_3 import unique_names_func


class TestUniqueNamesFunc(unittest.TestCase):

    def setUp(self):
        # Используем существующие данные из задания
        self.courses = [
            "Python-разработчик с нуля",
            "Java-разработчик с нуля",
            "Fullstack-разработчик на Python",
            "Frontend-разработчик с нуля",
        ]
        self.mentors = [
            [
                "Евгений Шмаргунов",
                "Олег Булыгин",
                "Дмитрий Демидов",
                "Кирилл Табельский",
                "Александр Ульянцев",
                "Александр Бардин",
                "Александр Иванов",
                "Антон Солонилин",
                "Максим Филипенко",
                "Елена Никитина",
                "Азамат Искаков",
                "Роман Гордиенко",
            ],
            [
                "Филипп Воронов",
                "Анна Юшина",
                "Иван Бочаров",
                "Анатолий Корсаков",
                "Юрий Пеньков",
                "Илья Сухачев",
                "Иван Маркитан",
                "Ринат Бибиков",
                "Вадим Ерошевичев",
                "Тимур Сейсембаев",
                "Максим Батырев",
                "Никита Шумский",
                "Алексей Степанов",
                "Денис Коротков",
                "Антон Глушков",
                "Сергей Индюков",
                "Максим Воронцов",
                "Евгений Грязнов",
                "Константин Виролайнен",
                "Сергей Сердюк",
                "Павел Дерендяев",
            ],
            [
                "Евгений Шмаргунов",
                "Олег Булыгин",
                "Александр Бардин",
                "Александр Иванов",
                "Кирилл Табельский",
                "Александр Ульянцев",
                "Роман Гордиенко",
                "Адилет Асканжоев",
                "Александр Шлейко",
                "Алена Батицкая",
                "Денис Ежков",
                "Владимир Чебукин",
                "Эдгар Нуруллин",
                "Евгений Шек",
                "Максим Филипенко",
                "Елена Никитина",
            ],
            [
                "Владимир Чебукин",
                "Эдгар Нуруллин",
                "Евгений Шек",
                "Валерий Хаслер",
                "Татьяна Тен",
                "Александр Фитискин",
                "Александр Шлейко",
                "Алена Батицкая",
                "Александр Беспоясов",
                "Денис Ежков",
                "Николай Лопин",
                "Михаил Ларченко",
            ],
        ]

    def tearDown(self):
        del self.courses
        del self.mentors

    def test_returns_string(self):
        """Тест: функция возвращает строку"""
        result = unique_names_func(self.courses, self.mentors)
        self.assertIsInstance(result, str)

    def test_contains_all_unique_names(self):
        """Тест: результат содержит все уникальные имена"""
        result = unique_names_func(self.courses, self.mentors)

        # Проверяем наличие ожидаемых имен
        expected_names = [
            "Адилет",
            "Азамат",
            "Александр",
            "Алексей",
            "Алена",
            "Анатолий",
            "Анна",
            "Антон",
            "Вадим",
            "Валерий",
            "Владимир",
            "Денис",
            "Дмитрий",
            "Евгений",
            "Елена",
            "Иван",
            "Илья",
            "Кирилл",
            "Константин",
            "Максим",
            "Михаил",
            "Никита",
            "Николай",
            "Олег",
            "Павел",
            "Ринат",
            "Роман",
            "Сергей",
            "Татьяна",
            "Тимур",
            "Филипп",
            "Эдгар",
            "Юрий",
        ]
        for name in expected_names:
            self.assertIn(name, result)

    def test_no_duplicates_in_result(self):
        """Тест: в результате нет дубликатов имен"""
        result = unique_names_func(self.courses, self.mentors)
        result_list = result.split(", ")

    def test_sorted_alphabetically(self):
        """Тест: имена отсортированы по алфавиту"""
        result = unique_names_func(self.courses, self.mentors)
        result_list = result.split(", ")

        # Проверяем, что список отсортирован
        self.assertEqual(result_list, sorted(result_list))

    def test_specific_names_count(self):
        """Тест: проверка количества уникальных имен"""
        result = unique_names_func(self.courses, self.mentors)
        result_list = result.split(", ")

        # Проверяем точное количество
        n = 33
        self.assertEqual(len(result_list), n)

    def test_empty_input(self):
        """Тест: обработка пустых данных"""
        empty_result = unique_names_func([], [])
        self.assertEqual(empty_result, "")

    def test_format_correct(self):
        """Тест: правильный формат вывода (через запятую и пробел)"""
        result = unique_names_func(self.courses, self.mentors)

        # Проверяем формат
        self.assertIn(", ", result)

        # Первое имя не должно начинаться с запятой и с пробела
        self.assertNotEqual(result[0], ",")
        self.assertNotEqual(result[0], " ")
