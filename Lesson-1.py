#Задание 1
number = int(input("Введите число: "))
print(number)
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
print("Привет, ", name, surname)

#Задание 2
sec = int(input("Введите время в секундах: "))
sec %= (24 * 3600)
hour = sec // 3600
sec %= 3600
min = sec // 60
sec %= 60
print("%02d:%02d:%02d" % (hour, min, sec))

#Задание 3
n = int(input('Введите целое положительное число: '))
print(n + n*11 + n*111)

#Задание 4
x = int(input('Введите целое положительное число: '))
y = -1
while x > 1:
    z = x % 10
    x //= 10
    if z > y:
        y = z
print('Самая большая цифра в числе:', y)

#Задания 5,6
sales = int(input('Введите сумму выручки: '))
expenses = int(input('Введите сумму расходов: '))
balance = sales - expenses
if balance < 0:
    print('Фирма работает в убыток: ', balance)
elif balance == 0:
    print('Фирма работает в 0')
elif balance > 0:
    print('Фирма работает с прибылью: ', balance)
    print("Рентабельность: %.0f%%" % (balance / sales * 100))
    personal = int(input('Введите количество сотрудников: '))
    print("Прибыль на 1 сотрудника: %.0f" % (balance / personal))

#Задание 7
a = int(input('Введите дистанцию за 1-й день: '))
b = int(input('Введите желаемую дистанцию: '))
day = 1
while a < b:
    a *= 1.1
    day += 1
print('Желаемый результат будет достигнут через %s дней' % day)