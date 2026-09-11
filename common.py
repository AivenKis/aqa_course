#                                                Урок 1: Основы функций
#                                                           Цель:
#                               Понять, как устроены функции, как они принимают данные и как их использовать.
# from requests_toolbelt.multipart.encoder import total_len
#
#
# def get_user_name(prompt: str, min_length=3) -> str:
#
#     while True:
#         user_input = input(prompt).strip()
#
#         if not user_input:
#             print("ERROR: Значение не может быть пустым.\n")
#             continue
#
#         if len(user_input) < min_length:
#             print(f"ERROR: Значение должно содержать не менее {min_length} символов.\n")
#             continue
#
#         return user_input
import re
from idlelib.replace import replace

# Вызов функции:
#                       → Функция стала универсальной, потому что теперь вызывающий код решает, КАКАЯ МИНИМАЛЬНАЯ ДЛИНА
#                                            НУЖНА В КАЖДОМ КОНКРЕТНОМ СЛУЧАЕ.

# # 1. Получить имя
# first_name = get_user_name("Введите ваше имя: ")
#
# # 2. Получить фамилию
# last_name = get_user_name("Введите вашу фамилию: ")
#
# # 3. Поменять порядок: Фамилия + Имя
# reversed_name = f"{last_name} {first_name}"
#
# # 4 Перевести результат в верхний регистр
# upper_name = reversed_name.upper()
#
# # 5 Посчитать длину: длина_имени + длина_фамилии + 1 (пробел)
# total_length = len(first_name) + len(last_name) + 1
#
# # 6. Красиво вывести результат
#
# print("\n" + "=" * 50)
# print(f"В обратном порядке:     {reversed_name}")
# print(f"Заглавными:             {upper_name}")
# print(f"Длина строки:           {total_length}")
# print("=" * 50)







"""
Важные моменты, которые нужно понять:
    1. Функция greet_user() должна только возвращать имя. Она не должна сама печатать приветствие. Приветствие лучше выводить снаружи.
    2. Type hint пишется как prompt: str, а не как текст подсказки.
    3. Когда функция принимает параметр — его обязательно нужно передавать при вызове.


Главный смысл:

Мы передаём prompt, чтобы функция не знала, что именно спрашивать. Она просто "инструмент для получения строки от пользователя". 
А что спрашивать — решает тот, кто вызывает функцию.

Это делает функцию:
    ✔️ Гибкой
    ✔️ Переиспользуемой
    ✔️ Более "чистой" (она делает только одну вещь — получает строку)

Это один из важнейших принципов программирования — Separation of Concerns (разделение ответственности).


Зачем мы вызываем функцию через name = greet_user(...), а не просто greet_user(...)?

 Программа просто потеряет результат, который вернула функция. То есть функция отработает, вернёт имя, но мы его никуда не сохраним.

Правильно:

    name = greet_user(...) — мы сохраняем результат в переменную.
    greet_user(...) — функция отработает, но результат будет потерян.

"""

# # объявляем функцию, передаем в нее аргумент text, тип string. Функция возвращает булево значение
# def is_palindrome(text:str) -> bool:
#
# # объявляем переменную cleaned, приводим ее значение к нижнему регистру и удаляем пробелы
#    cleaned = text.lower().replace(" ", "")
#
# #  разворачиваем значение строки
#    reversed_text = cleaned[::-1]
#
#
# # ПРОВЕРКА ЧТО  ПОЛУЧЕННОЕ ЗНАЧЕНИЕ ЯВЛЯЕТСЯ ПАЛИДРОМОМ
#    if cleaned == reversed_text:
#        return True
#    else:
#        return False
#
#
# while True:
#     user_input = input("Enter a string check: ").strip()
#
#     if not user_input:
#         print("The string cannot be empty. \n")
#         continue
#
#     result = is_palindrome(user_input)
#
#     if result:
#         print("The string is palindrome. \n")
#
#     else:
#         print("The string is not palindrome. \n")
#
#     break

text = "PythonProgramming"
print(text[:6])
print(text[-3:])
print(text[::2])





