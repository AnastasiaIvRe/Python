"""
Задание 2. Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.

"""

with open('task02.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f"Всего строк: {len(lines)}")
    for key, value in enumerate(lines):
        words = value.split(' ')
        print(f"Слов в строке {key + 1}: {len(words)}")
