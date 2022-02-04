#Задание 1
from sys import argv
name, hours, rate, bonus = argv
salary = (int(hours) * int(rate)) + int(bonus)
print(f'Заработная плата сотрудника {name}: {salary}')

#Задание 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')

#Задание 3
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

#Задание 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

#Задание 5
from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el
print(f'Список чётных чисел от 100 до 1000: {my_list}')
print(f'Результат перемножения всех элементов списка: {reduce(my_func, my_list)}')

#Задание 6.1
from itertools import count

def my_count_func(start_num, stop_num):
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)
my_count_func(int(input('Введите стартовое число: ')), int(input('Введите конечное число: ')))

#Задание 6.2
from itertools import cycle

my_list = [1, 2, 3, 4]
def my_cycle_func(my_list, iteration):
    c = 0
    for el in cycle(my_list):
        if c > iteration:
            break
        print(el)
        c += 1
my_cycle_func(my_list, int(input('Введите количество повторений: ')))

#Задание 7
from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break