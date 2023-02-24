"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно,
в программе.
"""

list_1 = [10, 1.3, True, "Hi", None]
for el in list_1:
    print(type(el))

"""
Задание 2. Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
"""
list_2 = input("Введите целые числа через пробел:").split(' ')
a, b = 1, 2
while len(list_2) > b:
    list_2[a], list_2[b] = list_2[b], list_2[a]
    a += 3
    b += 3
print('Результат:', *list_2)

"""
Задание 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
# Решение 1

month = int(input("Введите номер месяца: "))
list_3 = [
    "Зима",
    "Зима",
    "Весна",
    "Весна",
    "Весна",
    "Лето",
    "Лето",
    "Лето",
    "Осень",
    "Осень",
    "Осень",
    "Зима"]

print(f'Результат_1: {list_3[month - 1]}')

# Решение 2

month = int(input("Введите номер месяца: "))

dict_1 = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
          6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень",
          11: "Осень", 12: "Зима"}
print(f'Результат_2: {dict_1.get(month)}')

""" 
Задание 4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове. 
"""
list_4 = input("Введите слова через пробел: ").split()
k = 0
for word in list_4:
    k += 1
    if len(str(word)) > 10:
        print("<", k, "строка >", str(word)[0:10])
    else:
        print("<", k, "строка >", word)

""" 
Задание 5.
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
"""
rating = [7, 5, 3, 3, 1]
print(f"Текущий рейтинг: {rating}")

new_scores = int(input("Сколько новых элементов рейтинга вы хотите указать: "))

for i in range(1, new_scores + 1):
    new_score = int(input("Введите новый элемент рейтинга: "))
    if new_score > 0:
        rating.append(new_score)
        rating.sort(reverse=True)
        print(f"Новый рейтинг: {rating}")
    else:
        print("Ошибка. Вы ввели не корректное число")

"""
Задание 6. Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами,
то есть характеристиками товара: название, цена, количество, единица измерения.
Структуру нужно сформировать программно, запросив все данные у пользователя.
"""

goods = []
analytics = {'name': [],
             'price': [],
             'quantity': [],
             'unit': []}
num = 1
while True:
    name = input('Введите название товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    unit = input('Введите единицу измерения товара: ')
    params = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'unit': unit
    }
    good = (num, params)
    goods.append(good)

    for key, value in params.items():
        i = analytics.get(key)
        if value in i:
            continue
        i.append(value)
        continue

    num += 1
    exit_answer = input('Ввести еще позицию? да, нет: ').lower()
    if exit_answer == 'нет':
        break
print(analytics)

list_6 = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
          (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
          (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]

names_lst = []
price_lst = []
counts_lst = []
units_lst = []
res_dict = {}
for i in range(len(list_6)):
    names_lst.append(list_6[i][1]['название'])
    price_lst.append(list_6[i][1]['цена'])
    counts_lst.append(list_6[i][1]['количество'])
    units_lst.append(list_6[i][1]['ед'])

res_dict.update({'Название': names_lst, 'Цена': price_lst, 'Количество': counts_lst, 'Единицы': units_lst})
print(res_dict)

