#Задание 1
list = [1, 'школа', 3.14]
for i in list:
    print(type(i))

#Задание 2
list = input('Введите элементы списка: ').split()
list[:-1:2], list[1::2] = list[1::2], list[:-1:2]
print(list)

#Задание 3 (list)
season_list = ['зима', 'весна', 'лето', 'осень']
month = int(input('Введите месяц в виде числа: '))
if month == 1 or month == 2 or month == 12:
    print('Время года: %s' % season_list[0])
elif month == 3 or month == 4 or month == 5:
    print('Время года: %s' % season_list[1])
elif month == 6 or month == 7 or month == 8:
    print('Время года: %s' % season_list[2])
elif month == 9 or month == 10 or month == 11:
    print('Время года: %s' % season_list[3])
else:
    print('Нет такого месяца!')

#Задание 3 (dict)
season_dict = {
    "зима": (1, 2, 12),
    "весна": (3, 4, 5),
    "лето": (6, 7, 8),
    "осень": (9, 10, 11)
}
month = int(input('Введите месяц в виде числа: '))
for key in season_dict.keys():
    if month in season_dict[key]:
        print('Время года: %s' % [key])

#Задание 4
words = input('Введите слова через пробел: ').split()
for i in range(len(words)):
    if len(str(words)) <= 10:
        print(i+1, words[i])
    else:
        print(i+1, words[i][0:10])

#Задание 5
my_list = [7, 5, 3, 3, 2]
print(f'Рейтинг: {my_list}')
number = int(input('Введите новый элемент рейтинга: '))
for i in range(len(my_list)):
    if my_list[i] == number:
        my_list.insert(i + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
        break
    elif my_list[-1] > number:
        my_list.append(number)
        break
    elif my_list[i] > number and my_list[i + 1] < number:
        my_list.insert(i + 1, number)
        break
print(f'Новый рейтинг: {my_list}')

#Задание 6
goods = []
number = 0
while input("Добавить новый товар? (да/нет): ") == 'да':
    number += 1
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    amount = input('Введите количество товара: ')
    unit = input("Введите единицу измерения: ")
    features = {'Название': name, 'Цена': price, 'Количество': amount, 'eд': unit}
    goods.append(tuple([number, features]))
else:
    print(*goods, sep='\n')

#analytics = {"Название": features[name], "Цена": features[price], "Количество": features[amount], "ед": features[unit]}
#print(analytics)

#Вторую часть шестого задания решить не удалось