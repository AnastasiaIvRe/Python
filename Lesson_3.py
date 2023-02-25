"""
Задание 1.  Реализовать функцию,
принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.

"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Результат"


try:
    n1 = float(input("a = "))
    n2 = float(input("b = "))
    print(f"a / b = {divide(n1, n2)}")
except ValueError:
    print("Неверно введенное значение")

"""
 Задание 2. Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой. 

"""


def personal_data(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')


personal_data(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)

"""
Задание 3.  Реализовать функцию my_func(), 
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

"""


# Вариант 1

def my_func(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c


try:
    n1 = int(input("a = "))
    n2 = int(input("b = "))
    n3 = int(input("c = "))
    print(f"The sum of the two maximum numbers:  {my_func(n1, n2, n3)}")
except ValueError as e:
    print(f"{e}")


# Вариант 2

def find_max(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))


find_max(3, 5, 7)

"""
Задание 4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

"""


def my_abc(x):
    return x if x >= 0 else x * -1


def raising_to_power(x, y):
    result = x
    for i in range(my_abc(y) - 1):
        result *= x
    if y < 0:
        result = 1 / result
    return result


try:
    basis = int(input("x = "))
    degree = int(input("y = "))
    print(f"x ** y =  {raising_to_power(basis, degree)}")
except ValueError as e:
    print(e)

""" Задание 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

"""


def my_sum(my_list):
    items_sum = 0
    for item in my_list:
        try:
            items_sum += float(item)
        except ValueError:
            continue
    return items_sum


def sum_my_string(a):
    a = a.replace('*', '')
    a = a.replace(',', '.')
    numbers = a.split(' ')
    return my_sum(numbers)


numbers_sum = 0

while True:
    numbers_sting = input("Введите строку чисел, разделенных пробелом. Для завершения введите символ '*'\n")
    numbers_sum += sum_my_string(numbers_sting)
    if numbers_sum != 0:
        print(f"Сумма значений элементов {numbers_sum}")
    if numbers_sting.count('*') > 0:
        break

"""
Задание 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.
Задание 7.Продолжить работу над заданием.
В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().

"""


def int_func(words: str):
    first_char = words[:1]
    big_first_char = first_char.upper()
    tail = words[1:]
    return big_first_char + tail


def int_func_ext(row: str):
    result = []
    words = row.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Введите строку для преобразования:\n")
print(f"{int_func_ext(s)}")
