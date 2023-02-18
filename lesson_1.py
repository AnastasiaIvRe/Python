# Задание 1
a = "Привет, Мир"
b = "Уже февраль,"
c = "скоро весна!"
print(a,b,c)

txt = input("Введите ваше имя: ")
print("Добрый день, ", txt)

nmr = int(input("Введите ваш возраст: "))
print("Возраст, ", nmr)

# Задание 2
def time (sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)
k = input("Ведите количество секунд: ")
n = int(k)
print("Time in preferred format: ", time(n))

# Задание 3
n = int(input("Введите n:"))
k = str(n)
k1 = k + k
k2 = k + k + k
sum = n + int(k1) + int(k2)
print("Результат: ", sum)

# Задание 4
a = int(input("Введите число: "))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

# Задание 5 и 6
profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабильность выручки составила {profit / costs:.2f}")
    rab = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сотрудника составила {profit / rab:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

# Задание 7
x = int(input("Результаты пробежки в первый день (в км): "))
y = int(input("Общий желаемый результат (в км): "))
i = 1
while x < y:
    x *= 1.1
    i += 1
print("Вы достигнете результата на ", i, "день")

